"""
This programs is a basic one to learn about traversing a string and counting, comparing etc
"""

import re


def count_words(s):
    char_count = 0
    word_count = 0
    vowels_count = 0
    consonants_count = 0

    s_length = len(s)

    in_word = False

    vowels = {'a', 'e', 'i', 'o', 'u'}

    for i in range(s_length):
        char_count += 1
        if s[i] == ' ':
            in_word = False
        else:
            if not in_word:
                word_count += 1
                in_word = True  # Now we are inside a word

        valid_pattern = r'[a-zA-Z]'
        if (re.findall(valid_pattern, s[i])):
            if s[i].lower() in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print("Summary for the sentence - ", s)
    print("Total number of characters: ", char_count)
    print("Total number of words: ", word_count)
    print("Total number of vowels: ", vowels_count)
    print("Total number of consonants: ", consonants_count)

    print("\n", end="")


if __name__ == "__main__":
    s1 = "My name is Shashank"

    s2 = "My name is                    Shashank"

    s3 = "   My name is                    Shashank  "

    count_words(s1)
    count_words(s2)
    count_words(s3)
