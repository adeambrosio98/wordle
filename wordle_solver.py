from english_words import english_words_lower_alpha_set
from wordle import (
    MAX_TRIES,
    get_5_letter_words,
    get_mask_correct_letters,
    get_mask_existing_letters,
)
from random import choice


def filter_words(guess, five_letter_words, correct_mask, existing_mask):
    for index, letter in enumerate(guess):
        if correct_mask[index]:
            #five_letter_words = [word for word in five_letter_words if word[index] == letter]

            #five_letter_words = filter(lambda word, index=index, letter=letter: word[index] == letter, five_letter_words)

            for word in five_letter_words:
                if word[index] != letter:
                    five_letter_words.remove(word)

        if not existing_mask[index]:
            #five_letter_words = [word for word in five_letter_words if letter not in word]

            #five_letter_words = filter(lambda word, letter=letter: letter not in word, five_letter_words)

            for word in five_letter_words:
                if letter in word:
                    five_letter_words.remove(word)

        if existing_mask[index]:
            #five_letter_words = [word for word in five_letter_words if letter in word]

            #five_letter_words = filter(lambda word, letter=letter: letter in word, five_letter_words)

            for word in five_letter_words:
                if letter not in word:
                    five_letter_words.remove(word)

    return five_letter_words


if __name__ == "__main__":
    five_letter_words = get_5_letter_words(all_words=english_words_lower_alpha_set)
    print(f"there are {len(five_letter_words)} words")

    right_word = choice(five_letter_words)
    print(f"the word you're trying to guess is: {right_word}")

    guess = "piano"
    print(f"the first guess is {guess}")

    number_of_tries = 1

    while number_of_tries <= MAX_TRIES:
        if guess == right_word:
            print("congrats! you found the right word")
            exit()

        correct_mask = get_mask_correct_letters(guess, right_word)
        existing_mask = get_mask_existing_letters(guess, right_word)

        five_letter_words = filter_words(
            guess, five_letter_words, correct_mask, existing_mask
        )
        print(f"there are {len(five_letter_words)} possible words")

        guess = choice(five_letter_words)
        number_of_tries += 1
        print(f"the tried word is {guess}. you have made {number_of_tries} tries")

    print("loser, no more tries")
