"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""


# Brute Force method - O(n^3)
def three_sum_1(nums):
    size = len(nums)
    result = []
    for i in range(size):
        for j in range(i, size):
            for k in range(j, size):
                if nums[i] + nums[j] + nums[k] == 0 and i != j and j != k and i != k:
                    to_add = sorted([nums[i], nums[j], nums[k]])
                    if to_add not in result:
                        result.append(to_add)
    return result


def three_sum_2(nums):
    # sort the array
    sorted_nums = sorted(nums)

    for i in range(len(nums)-1):
        nums[i] + nums[i+1]


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0]
    # nums = [0, 2, 3]

    print(three_sum_1(nums))
