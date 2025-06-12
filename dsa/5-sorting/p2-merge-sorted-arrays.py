# Source: EPI
# Difficulty: Easy
# Topic: Sorting
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..
"""
Given two sorted arrays A and B, merge the arrays
1. in A
2. in new array C
"""


def merge_C(A, B):
    i, j,  C = 0, 0, []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i = i+1
        elif B[j] < A[i]:
            C.append(B[j])
            j = j+1
        else:
            # equal
            C.append(A[i])
            C.append(B[j])

            i, j = i+1, j+1

    while i < len(A):
        C.append(A[i])
        i = i+1

    while j < len(B):
        C.append(B[j])
        j = j+1

    return C


def merge_A(A, B, m, n):
    # without creating any auxilliary space we merge A and B into A
    writer_idx = m+n-1

    i, j = m-1, n-1

    while i > 0 and j > 0:
        if B[j] > A[i]:
            A[writer_idx] = B[j]
            j = j-1

        else:
            A[writer_idx] = A[i]
            i = i-1

        writer_idx -= 1

    while j >= 0:
        A[writer_idx] = B[j]
        j = j-1
        writer_idx -= 1
    return


if __name__ == "__main__":
    A = [3, 13, 17]
    B = [3, 7, 11, 19]
    # print("Merged A and B", merge_C(A, B))

    # merging in A only
    m = len(A)
    n = len(B)
    A = A + [0]*n  # make space in A for B
    merge_A(A, B, m, n)
    print("Merged A and B", A)
