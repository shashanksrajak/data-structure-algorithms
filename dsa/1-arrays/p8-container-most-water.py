# Source: https://neetcode.io/problems/max-water-container?list=blind75
# https://leetcode.com/problems/container-with-most-water/submissions/1651960411/
# Difficulty: Medium
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        size = len(heights)
        width = size - 1
        i, j = 0, size - 1
        areas = []
        while i < j:
            area = 0
            if heights[i] < heights[j]:
                area = heights[i] * width
                i += 1
            else:
                area = heights[j] * width
                j -= 1
            areas.append(area)
            width -= 1
        return max(areas)
