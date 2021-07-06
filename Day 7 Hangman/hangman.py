# Day 7 of 100 Days of Code
# Starting code provided by Dr. Angela Yu
# Step 5
# TODO: Empty string will restart the game, Guessing correct letter will print it twice
import hangman_words as hw
import hangman_art as ha
import random

game_not_done = True

while game_not_done:
    # TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
    chosen_word = random.choice(hw.word_list)
    word_length = len(chosen_word)

    end_of_game = False

    lives = 6
    incorrect_letters = []

    # TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
    print(ha.logo)
    # Testing code
    # print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        print(f"{' '.join(display)}\n")
        guess = input("Guess a letter: ").lower()

        # Edge case: If the input is more than one letter, print out message to the player and prompt them to guess
        # again.
        if len(guess) > 1:
            print("You can only guess one letter at a time.")
            continue

        # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in display:
            print(f"You already guessed the letter {guess}.")
            print(f"Incorrect letters: {' '.join(incorrect_letters)}")
            print(ha.stages[lives])

            continue

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                print(f"{guess} is in the word.")
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the
            #  word.
            print(f"The letter {guess} is not in the word.")

            # Check to see if player already guessed an incorrect letter
            if guess in incorrect_letters:
                print(f"You already guessed the wrong letter {guess}.")
                print(f"Incorrect letters: {' '.join(incorrect_letters)}")
                print(ha.stages[lives])
                continue

            # add incorrect letters to incorrect_letters list
            incorrect_letters.append(guess)
            print(f"Incorrect letters: {' '.join(incorrect_letters)}")

            lives -= 1
            if lives == 0:
                # end_of_game = True
                print(ha.stages[lives])
                print(f"The word was: {chosen_word}.")
                print("You lose.")
                break

        # Join all the elements in the list and turn it into a String.
        # print(f"{' '.join(display)}")

        # Join all incorrect letters into a string and print to console
        # print(f"Incorrect letters: {' '.join(incorrect_letters)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print(f"{' '.join(display)}")
            print("You win!")
            break

        # TODO-2: - Import the stages from hangman_art.py and make this error go away.
        print(ha.stages[lives])

    start_over = True
    while start_over:
        play_again = input("Do you want to play again? (y)es or (n): ").lower()
        if play_again == "y":
            break
        elif play_again == 'n':
            game_not_done = False
            start_over = False
            print("Thank you for playing!")
            quit()
        else:
            print("invalid input.")
            continue
