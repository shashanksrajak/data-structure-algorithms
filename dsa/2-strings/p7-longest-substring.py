# Source: https://neetcode.io/problems/longest-substring-without-duplicates?list=blind75
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Difficulty: Easy
# Topic: Arrays
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len = 0
        l, r = 0, 0

        while r < len(s):
            if s[r] in char_set:
                l = l + 1
                r = l
                char_set.clear()
            else:
                char_set.add(s[r])
                r = r + 1
            max_len = max(r - l, max_len)

        return max_len

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
