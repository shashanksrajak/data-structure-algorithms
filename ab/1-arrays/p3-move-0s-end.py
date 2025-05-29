"""
Write a program in C to move all zeroes to the end of a given array.

Input:

2 5 7 0 4 0 7 -5 8 0

Output:

2 5 7 8 4 -5 7 0 0 0
"""


def move_zeroes(A):
    """
    T: O(n) S: O(1)
    """
    reader, writer = 0, len(A)-1

    while reader < writer:
        if A[reader] == 0:
            # swap
            A[reader], A[writer] = A[writer], A[reader]
            reader, writer = reader+1, writer-1
        if A[reader] != 0:
            reader += 1
        if A[writer] == 0:
            writer -= 1


A = [2, 5, 7, 0, 4, 0, 7, -5, 8, 0]
print("Original A", A)

move_zeroes(A)

print("A after moving 0s", A)
