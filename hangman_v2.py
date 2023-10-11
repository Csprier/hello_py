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

    for i in random_word:
        while True:
            # Ask the user to guess a letter
            guess = input("Choose a letter! ").lower() # Bonus - make the input lower case
            if len(guess) == 1:
                 # need to limit user_guesses to not exceed values of random_word_dict
                    for letter, frequency in user_guesses.items():
                        if letter in random_word_dict and random_word_dict[letter] >= user_guesses[letter]:
                            print(f"The letter occurs more than once. You do not need to guess this letter again. :)")
                            print(f"user_guesses[letter]: {user_guesses[letter]} = random_word_dict[letter]: {random_word_dict[letter]}")
                            user_guesses[letter] = random_word_dict[letter]
                            break
                        else:
                            user_guesses[guess] += 1
                            break
            else:
                print("Single letters only.")
                continue

    print(f"user_guesses: ", user_guesses)

    # ===============================================================================================
    
             

    # ===============================================================================================    
    # Check if the dict's are the same
    are_equal = True
    for key, value in user_guesses.items():
        if key in random_word_dict and random_word_dict[key] == value:
            continue
        else:
            are_equal = False;
            break

    if are_equal == True:
        print(f"Congratulations! The letters you chose spell the word '{random_word}'! The man will not be hanged!")
    else:
        print(f"You failed to spell '{random_word}'. HANG HIM!")

    # ===============================================================================================
    # Play again or exit the game
    play_again = input("Would you like to play again? y / n : ")

    if play_again == "y":
        hangman()
    else:
        print("That's enough executions for one day. See you next time.")

hangman()
