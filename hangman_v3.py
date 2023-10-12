# ===============================================================================================
# ===== imports ===== #
import random
from collections import Counter

# ===============================================================================================
# Main function
# ---------------------------
def hangman():
    # ===============================================================================================
    # Create a greeting
    print("======================================================================================")
    print("= Greetings! Welcome to Hangman! Save the man's life by guessing correctly! Good luck! ")
    print("======================================================================================")
    print("= Rules:")
    print("= Players get 3 chances to guess.")
    print("= There is no penalty for correct guesses, or repeated guesses.")
    print("= Every missed letter is -1 chance. Get to 0 and the man hangs!")
    print("======================================================================================")
    # ===============================================================================================
    # Create word list
    word_list = ["pickles", "stank", "heck", "meat", "bologna", "apple", "banana"]
    
    # Randomly choose a word from the list you have created
    random_word = random.choice(word_list)
    
    # Make a pre-existing dict of the word to cross reference
    random_word_dict = Counter(random_word)

    # Make a counter for the user guesses key-value/ letter-frequency
    user_guesses = Counter()

    # How many chances a player has to guess
    chance_count = 3
    # ===============================================================================================
    # Main loop
    # ===============================================================================================
    for i in random_word:
        while True:
            # Display remaining chances
            print(f"- You have {chance_count} chances remaining!")

            # Has the user spelled the word with all their previous guesses?
                # If yes, win the game
            if set(user_guesses.items()) == set(random_word_dict.items()):
                print('-------------------------------------------')
                print(f"- ! Congratulations! You won the game! The man's life is spared! !")
                print('-------------------------------------------')
                return # hard exit loop and function
            
            # If a user runs out of chances to guess, they lose!
            if chance_count == 0:
                print('--------------------------------------------------------------------------------------------------')
                print(f"- X The man hangs because of your inability to guess correctly! The word was '{random_word}'. X -")
                print('--------------------------------------------------------------------------------------------------')
                return # hard exit loop and function

            # Ask the user to guess a letter
            guess = input("Choose a letter! ").lower() # Bonus - make the input lower case

            # If the length of the guess is 1, continue.
            if len(guess) == 1:
                # Have we guessed this letter already?
                    # If yes, user_guesses should reflect this with a higher frequency. Thus we let the user know they have already guessed this letter.
                    # If no, no penalty
                if guess in user_guesses:
                    print('-------------------------------------------')
                    print(f"- You've guessed '{guess}' already! Guess correctly before you run out of chances!")
                    print('-------------------------------------------')
                    continue

                # Is the guess part of the random word?
                    # If yes, continue. Update user_guesses. Players only need to guess a letter once.
                    # If no, chances_count - 1
                if guess in random_word: # if yes
                    print('-------------------------------------------')
                    print(f"- You successfully guessed a letter in the word!")
                    print('-------------------------------------------')
                    user_guesses[guess] = random_word_dict[guess]
                    chance_count -= 1
                    continue
                else: # if no
                    print('-------------------------------------------')
                    print(f"- Sorry! That letter is not part of the word!")
                    print('-------------------------------------------')
                    chance_count -= 1
                    continue
            # If the length of the guess > 1, it can't be accepted as a valid input.
            else:
                print('-------------------------------------------')
                print("- Single letters only.")
                print('-------------------------------------------')
                continue

    # ===============================================================================================
    # Play again or exit the game
    play_again = input("Would you like to play again? y / n : ")
    if play_again == "y":
        hangman()
    else:
        print("That's enough executions for one day. See you next time.")

hangman()