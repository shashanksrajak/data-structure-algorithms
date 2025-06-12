# Source: https://neetcode.io/problems/longest-consecutive-sequence?list=blind75
# Difficulty: Medium
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        size = len(nums)

        if size < 2:
            return size

        # sort the array
        # we can also achieve O(n) instead of O(nlogn) by using count sort
        sorted_array = sorted(nums)

        max_size = 1
        running_max_size = 1

        for i in range(1, size):
            diff = sorted_array[i] - sorted_array[i-1]
            if diff == 1:
                running_max_size += 1
            elif diff == 0:
                continue
            else:
                if running_max_size > max_size:
                    max_size = running_max_size
                running_max_size = 1

        if running_max_size > max_size:
            max_size = running_max_size

        return max_size
