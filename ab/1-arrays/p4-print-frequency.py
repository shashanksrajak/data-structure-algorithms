"""
Write a program in C to find the number of times each unique number appears in an array.

-- Think if array is unsorted vs sorted. (Sorting brings similar elements together)

Input :

2 3 4 4 4 4 5 5 5 6 7 7

Output:

The number of times the number 2 occurs in the given array is: 1

The number of times the number 3 occurs in the given array is: 1

The number of times the number 4 occurs in the given array is: 4

The number of times the number 5 occurs in the given array is: 3

The number of times the number 6 occurs in the given array is: 1

The number of times the number 7 occurs in the given array is: 2
"""


def frequency_hashing(items):
    frequency_dict = {}

    for num in items:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    for key, value in frequency_dict.items():
        print(
            f"The number of times the number {key} appears in the array is: {value}")


"""
This will have T: O(n) but S: O(n), so we can think of better S
"""


def frequency_inplace(items):
    if not items:
        return None

    count = 1
    for i in range(len(items)-1):
        if items[i] == items[i+1]:
            count = count+1
        else:
            print(f"The number {items[i]} appears {count} times")
            count = 1

    print(f"The number {items[-1]} appears {count} times")


"""
T: O(n) S: O(1)
"""


A = [2, 3, 4, 4, 4, 4, 5, 5, 5, 6, 7, 8]

print("Original A", A)

# frequency_hashing(A)

frequency_inplace(A)
