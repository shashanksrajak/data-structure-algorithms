"""
Write a program in C to rotate an array by N positions.

Input:

0 3 6 9 12 14 18 20 22 25 27

4

Output:

After rotating from 4th position the array is:

12 14 18 20 22 25 27 0 3 6 9

Explanation :

The given array is : 0 3 6 9 12 14 18 20 22 25 27

From 4th position the values of the array are : 12 14 18 20 22 25 27

Before 4th position the values of the array are : 0 3 6 9

After rotating from 4th position the array is:

12 14 18 20 22 25 27 0 3 6 9

"""


"""
this method  works in O(n) but space is O(n)
"""


def rotate_1(A, rotation_index):
    return A[rotation_index:] + A[:rotation_index]


def rotate_2(A, rotation_index):
    """
    this approach uses reversal technique to rotate in place -> T: O(n) S: O(1)
    """

    # rotate the entire array
    i, j = 0, len(A)-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i, j = i+1, j-1

    i, j = 0, len(A)-rotation_index-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i, j = i+1, j-1

    i, j = len(A)-rotation_index, len(A)-1
    while i < j:
        A[i], A[j] = A[j], A[i]
        i, j = i+1, j-1


def reverse_sub_array(arr, start, end):
    """Helper function to reverse a portion of an array."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_reversals(arr, k):
    n = len(arr)
    if n == 0:
        return arr
    k = k % n  # Handle k > n

    # Step 1: Reverse the entire array
    reverse_sub_array(arr, 0, n - 1)

    # Step 2: Reverse the first k elements
    reverse_sub_array(arr, 0, k - 1)

    # Step 3: Reverse the remaining n-k elements
    reverse_sub_array(arr, k, n - 1)
    return arr


if __name__ == "__main__":
    A = [0, 3, 6, 9, 12, 14, 18, 20, 22, 25, 27]
    B = [0, 3, 6, 9, 12, 14, 18, 20, 22, 25, 27]

    print("Original Array ", A)
    print("Rotated Array ", rotate_1(A, 4))

    print("Original Array ", B)
    rotate_2(B, 4)
    print("Rotated Array ", B)
