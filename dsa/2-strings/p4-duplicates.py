"""
Find duplicates in a string
"""

"""
Multiple ways
1. Brute force - compare each char in both
2. Hashing - easy to implement, efficient but takes S: O(n)
3. Bitwise operations - using bits
"""


def find_duplicates_hashing(s):
    char_dict = {}

    for char in s.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    # traverse the dict and use the info to return response

    for key, value in char_dict.items():
        print(key, value)


find_duplicates_hashing("Shashank")
