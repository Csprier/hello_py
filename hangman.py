# ===============================================================================================
# create a greeting
# create your word list
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus make the program take the input from the user and make it lowercase
# check if the letter is in the word

# ===============================================================================================
# ===== imports ===== #
import random
from collections import Counter

# ===============================================================================================
# Helper function
def rearrange_string(random_string, word):
    # count the character frequencies in the random string and the word
    random_string_count = Counter(random_string)
    word_count = Counter(word)

    # Check if the character frequency in the random string are sufficient
    for char, count in word_count.items():
        if random_string_count[char] < count:
            return False
        
    return True

# ===============================================================================================
# Main function
def hangman():
    print("Greetings!")
    word_list = ["pickles", "stank", "heck"]
    random_word = random.choice(word_list)
    
    user_guesses = []
    user_letters = ""
    
    for i in random_word:
        letter_choice = input("Choose a letter! ").lower()
        user_guesses.append(letter_choice)

        if letter_choice in random_word:
            print(f"'{letter_choice}' is part of the word!")
        else:
            print(f"'{letter_choice}' is not part of the word!")

    user_letters = "".join(user_guesses)

    if (rearrange_string(user_letters, random_word) == True):
        print(f"The letters you chose spell the word '{random_word}'! The man will not be hanged!")
    else:
        print(f"You failed to spell '{random_word}'. HANG HIM!")


hangman()