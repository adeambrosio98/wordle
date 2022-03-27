from english_words import english_words_lower_alpha_set
from random import randint
from termcolor import colored

def get_5_letter_words(all_words):
    words_5 = []

    for word in all_words:
        if len(word) == 5:
            words_5.append(word)
    
    return words_5

def get_mask_correct_letters(user_input, right_word):
    mask_correct_letters = []
    for idx, letter in enumerate(user_input):
        mask_correct_letters.append(letter == right_word[idx])
    return mask_correct_letters

def get_mask_existing_letters(user_input, right_word):
    mask_existing_letters = []
    for letter in user_input:
        mask_existing_letters.append(letter in right_word)
    
    return mask_existing_letters

def get_colored_user_input(user_input, mask_correct_letters, mask_existing_letters):
    output = ""
    for idx, letter in enumerate(user_input):
        if mask_correct_letters[idx]:
            output += colored(letter, on_color="on_green")
        elif mask_existing_letters[idx]:
            output += colored(letter, on_color="on_yellow")
        else:
            output += letter
    
    return output

MAX_TRIES = 6

words_5 = get_5_letter_words(english_words_lower_alpha_set)

right_word = words_5[randint(0, len(words_5))]

tries = 0

while(tries < MAX_TRIES):
    user_input = input("Make your best guess: ")

    if len(user_input) != 5:
        print("❌ You stoopid! The word must be 5 letters long. ❌")
        continue

    if user_input == right_word:
        print("🎉 Yay! You are correct! 🎉")
        break

    if user_input not in words_5:
        print("❌ Word not valid! ❌")
        continue

    mask_correct_letters = get_mask_correct_letters(user_input, right_word)
    mask_existing_letters = get_mask_existing_letters(user_input, right_word)

    colored_user_input = get_colored_user_input(user_input, mask_correct_letters, mask_existing_letters)

    print(colored_user_input)
    tries += 1
    print(f"You got {MAX_TRIES-tries} left.")
