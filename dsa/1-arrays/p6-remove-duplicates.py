# Source: EPI 5.6
# Difficulty: Easy
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..
"""
Given an array (sorted), remove all the duplicate elements.
"""


def remove_duplicates(A):
    """
    This approach - updates the same array - S(n) = O(1) & T(n) = O(n)
    much better than the hashing method which will take O(n) auxilliary space

    two pointers - one writer and one reader
    """

    write_pointer = 0

    for read_pointer in range(1, len(A)):
        if A[write_pointer] != A[read_pointer]:
            write_pointer += 1
            A[write_pointer] = A[read_pointer]

    return write_pointer


def remove_duplicates_2(A):
    """this will work even well in unsorted array as opposed to above method which needs sorting
        but it will O(n) space, time is efficient O(n)

        it will return a new array, not an in-place ops
    """
    # store unique elements in A
    unique_elements = {}
    result = []

    for i in A:
        if i in unique_elements:
            unique_elements[i] += 1
        else:
            unique_elements[i] = 1

    for key in unique_elements.keys():
        result.append(key)

    return result


if __name__ == "__main__":
    # tests
    A1 = [2, 3, 3, 5, 7, 11, 11, 11, 13]
    B1 = [2, 3, 3, 5, 7, 11, 11, 11, 13]

    print("Original Array", A1)
    print("Removed duplicates", A1[:remove_duplicates(A1)+1])

    print("Original Array", B1)
    print("Removed duplicates", remove_duplicates_2(B1))
