"""
Write a program in C to find two elements whose sum is closest to zero.

Input:

38 44 63 -51 -35 19 84 -69 4 -46

Output:

The Pair of elements whose sum is minimum are:

44 -46
"""

"""
Brute force method - compare each pair. T: O(n^2) S: O(1)

Efficient method - sort the array and use 2 pointers
"""


def closest_sum(nums):
    n = len(nums)
    if n < 2:
        return

    i, j, min_sum = 0, n-1, float('inf')

    # sort the array
    nums.sort()

    result_pair = (nums[i], nums[j])

    while i < j:
        sum = nums[i] + nums[j]

        if abs(sum) < abs(min_sum):
            min_sum = sum
            result_pair = (nums[i], nums[j])

        if sum == 0:
            return result_pair
        elif sum < 0:
            i = i+1
        else:
            j = j-1

    return result_pair


if __name__ == "__main__":
    A = [38, 44, 63, -51, -35, 19, 84, -69, 4, -46]

    print("Original Array: ", A)
    print("Closest sum pair for 0 : ", closest_sum(A))
