# Source: EPI
# Difficulty: Easy
# Topic: Sorting
# Tags: arrays, sorting
# Related Concepts: ..
# Question: ..
"""
Given two sorted arrays find their intersection.
"""


def intersection(A, B):
    C = []
    i = 0
    j = 0

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            # to avoid duplicates
            if i == 0 or A[i] != A[i-1]:
                C.append(A[i])
            i += 1
            j += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1

    return C


if __name__ == "__main__":
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    C = intersection(A, B)
    print("intersection of A and B", C)
