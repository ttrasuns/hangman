import random


def random_word_from_list(word_list):
    random_word = random.randint(0, len(word_list)-1)
    return word_list[random_word]


def hangman_image(incorrect):
    hangman = ["  +———+",
               "  |   |",
               "  O   |"]
    print(hangman[0])
    print(hangman[1])
    if incorrect == 0:
        print("      |\n",
              "     |\n",
              "     |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 1:
        print("  O   |\n",
              "     |\n",
              "     |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 2:
        print("  O   |\n",
              " |   |\n",
              "     |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 3:
        print("  O   |\n",
              "/|   |\n",
              "     |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 4:
        print("  O   |\n",
              "/|\  |\n",
              "     |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 5:
        print("  O   |\n",
              "/|\  |\n",
              "/    |\n",
              "     |\n")
        print("\n========\n\n")
    elif incorrect == 6:
        print("  O   |\n",
              "/|\  |\n",
              "/ \  |\n",
              "     |\n")
        print("\n========\n\n")
    else:
        print("Drawing function error")
        quit()


def print_guessed_letters(letters):
    print("Guessed letters: ", end="")
    for letter in letters[:-1]:
        print(f"{letter}, ", end="")
    print(f"{letters[-1]}\n")


def get_guessed_letters(word, letters, previous_word=None):
    word_with_guessed = ''
    for letter in word:
        if letter in letters:
            word_with_guessed += letter
        else:
            word_with_guessed += '-'
    if previous_word == word_with_guessed:
        mistake = 1
    else:
        mistake = 0
    return word_with_guessed, mistake


def game_end_conditions(incorrect_guesses, guessed_word, word):
    if incorrect_guesses >= 6:
        hangman_image(6)
        print("You lost!\n")
        return False
    elif guessed_word == word:
        print("You won!\n")
        return False
    else:
        return True


game_state = None
word_list = ["chair", "helicopter", "cocacola"]

while game_state != "3":
    print("Enter 1 to play hangman, 2 to add a new word, 3 to quit program")
    game_state = input("Enter number: ")

    if game_state == "1":
        game_run = {
            "word": random_word_from_list(word_list),
            "guessed_letters": [],
            "state": True,
            "incorrect_guesses": 0,
            "guessed_word": ""
            }

        for character in game_run["word"]:
            game_run["guessed_word"] += "-"
        print("\n" + game_run["guessed_word"])

        print("\n")

        while game_run["state"]:
            hangman_image(game_run["incorrect_guesses"])
            letter = ""
            letter = input("Enter letter: ")

            if len(letter) != 1:
                print("Input a single letter!")
                continue
            elif letter in game_run["guessed_letters"]:
                print("You already guessed this letter!")
                print_guessed_letters(game_run["guessed_letters"])
                print(game_run["guessed_word"] + "\n")
                continue

            game_run["guessed_letters"].append(letter)
            print_guessed_letters(game_run["guessed_letters"])
            game_run["guessed_word"], mistake = get_guessed_letters(game_run["word"],
                                                game_run["guessed_letters"],
                                                game_run["guessed_word"])
            game_run["incorrect_guesses"] += mistake

            print(game_run["guessed_word"] + "\n")

            game_run["state"] = game_end_conditions(game_run["incorrect_guesses"],
                                game_run["guessed_word"],
                                game_run["word"])

    elif game_state == "2":
        new_word = input("Enter new word: ")
        word_list.append(new_word.lower())
        print(f"added {word_list[-1]}\n")

    elif game_state == "3":
        print("bye")

    else:
        print("Wrong choice!\n")
