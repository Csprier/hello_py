# ===============================================================================================
# ===== imports ===== #
import random
from collections import Counter

# ===============================================================================================
# Helper function
# ---------------------------
def rearrange_string(random_string, word):
    # Count the character frequencies in the random string and the word
    random_string_count = Counter(random_string)
    word_count = Counter(word)

    # Check if the character frequency in the random string are sufficient
    for char, count in word_count.items():
        if random_string_count[char] < count:
            return False
        
    return True

# ===============================================================================================
# Main function
# ---------------------------
def hangman():
    # Create a greeting
    print("====================================================================================================================")
    print(" Greetings! To save this man's life, you must guess the correct letters of a random word you don't know! Good luck! ")
    print("====================================================================================================================")

    # Create word list
    # word_list = ["pickles", "stank", "heck", "meat", "bologna", "apple", "banana"]
    word_list = ["apple", "banana", "moot"]
    
    # Randomly choose a word from the list you have created
    random_word = random.choice(word_list)
    print(random_word)
    
    # Make a pre-existing dict of the word to cross reference
    random_word_dict = Counter(random_word)
    print(f"random_word_dict: ", random_word_dict)

    # Make a counter for the user guesses key-value/ letter-frequency
    user_guesses = Counter()

    # How many chances a player has to guess
    chance_count = 3
    
    # ===============================================================================================
    # Main loop
    # ===============================================================================================
    for i in random_word:
        while True:
            # Has the user spelled the word with all their previous guesses?
                # If yes, win the game
            if set(user_guesses.items()) == set(random_word_dict.items()):
                print(f"Congratulations! You won the game! The man's life is spared!")
                break
            
            # If a user runs out of chances to guess, they lose!
            if chance_count == 0:
                print(f"The man hangs because of your inability to guess correctly!")
                break

            # Ask the user to guess a letter
            guess = input("Choose a letter! ").lower() # Bonus - make the input lower case
            # If the length of the guess is 1, continue.
            if len(guess) == 1:
                # Have we guessed this letter already?
                    # If yes, user_guesses should reflect this with a higher frequency. Thus we let the user know they have already guessed this letter.
                    # If no, no penalty
                if guess in user_guesses:
                    print(f"You've guessed '{guess}' already! No penalty for this, but guess something else!")
                    continue

                # Is the guess part of the random word?
                    # If yes, continue. Update user_guesses. Players only need to guess a letter once.
                    # If no, chances_count - 1
                if guess in random_word: # if yes
                    print(f"You successfully guessed a letter in the word!")
                    user_guesses[guess] = random_word_dict[guess]
                    print(f"::: {user_guesses}")
                    continue
                else: # if no
                    print(f"Sorry! That letter is not part of the word!")
                    chance_count - 1
                    continue
            # If the length of the guess > 1, it can't be accepted as a valid input.
            else:
                print("Single letters only.")
                continue

    print(f"user_guesses: ", user_guesses)
    print(f"Chances remaining: {chance_count}")

    # ===============================================================================================
    # Play again or exit the game
    play_again = input("Would you like to play again? y / n : ")
    if play_again == "y":
        hangman()
    else:
        print("That's enough executions for one day. See you next time.")

hangman()

# # ===============================================================================================    
# Check if the dict's are the same
# are_equal = True
# for key, value in user_guesses.items():
#     if key in random_word_dict and random_word_dict[key] == value:
#         continue
#     else:
#         are_equal = False;
#         break

# if are_equal == True:
#     print(f"Congratulations! The letters you chose spell the word '{random_word}'! The man will not be hanged!")
# else:
#     print(f"You failed to spell '{random_word}'. HANG HIM!") 