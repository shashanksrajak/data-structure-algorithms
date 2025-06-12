"""
Merge Sort Implementation

T : O(nlogn)
S: O(n) --> one disadvantage it we need auxilliary space to merge, that is merge problem, not sorting problem

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


def merge_sort(items):
    """
    items is the list to be sorted
    low: low index
    high: high index
    """

    # recursive base case -- it has only one element e.g. items = [4] and one element is always sorted
    if len(items) < 2:
        return items

    # find the mid where we need to divide into 2 halves
    mid = len(items) // 2

    # recursion part
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    return merge(left, right)


A = [64, 34, 25, 12, 22, 11, 90]

print("List A before sorting", A)

print("Sorted A : ", merge_sort(A))
