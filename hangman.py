# ===============================================================================================
# ===== imports ===== #
import random
from collections import Counter


# ===============================================================================================
# INSTRUCTIONS
# ---------------------------
# create a greeting
# create your word list
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word


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
    word_list = ["pickles", "stank", "heck", "meat", "bologna"]
    
    # Randomly choose a word from the list you have created
    random_word = random.choice(word_list)
    # print(random_word)
    
    # Ask the user to guess a letter
    user_guesses = []
    user_letters = ""
    
    # Check if the letter is in the word
    for i in random_word:
        letter_choice = input("Choose a letter! ").lower() # Bonus - make the input lower case
        user_guesses.append(letter_choice)
        # Make the list of letters into a single string
        user_letters = "".join(user_guesses)

        if letter_choice in random_word:
            # If the length of the user's letters is the same length as the random_word, there are no more guesses required
            if len(user_letters) != len(random_word):
                print(f"'{letter_choice}' is part of the word! Guess again!")
            else:
                # User helper function to determine is the guessed letters can be rearranged to the random word
                if (rearrange_string(user_letters, random_word) == True):
                    print(f"Congratulations! The letters you chose spell the word '{random_word}'! The man will not be hanged!")
                else:
                    print(f"You failed to spell '{random_word}'. HANG HIM!")
        # If the letter is not in the random_word, break out of the function
        else:
            print(f"'{letter_choice}' is not part of the word! You lose. He dies. Better luck next time.") 
            break

hangman()