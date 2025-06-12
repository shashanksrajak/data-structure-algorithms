"""
How to merge two sorted lists

It is easier to merge two sorted lists, if a problems asks merge two lists, its better to sort them first.

T : O(n)
S : O(n) --> we need an extra space to merge!!
"""


def merge(A, B):
    i, j = 0, 0

    size_A = len(A)
    size_B = len(B)

    merged_list = []

    while i < size_A and j < size_B:
        if A[i] < B[j]:
            merged_list.append(A[i])
            i = i+1
        else:
            merged_list.append(B[j])
            j = j+1

    merged_list.extend(A[i:])
    merged_list.extend(B[j:])

    return merged_list


A = [64, 34, 25, 12, 22, 11, 90]
B = [45, 33, 21, 89, 76, 15, 8]

sorted_A = sorted(A)
sorted_B = sorted(B)

result = merge(sorted_A, sorted_B)
print("Merged sorted list:", result)
