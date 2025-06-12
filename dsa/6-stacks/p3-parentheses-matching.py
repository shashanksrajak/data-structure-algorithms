# Source: https://leetcode.com/problems/valid-parentheses/description/
# Difficulty: Easy
# Topic: Stacks
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {
            "(": ")",
            "{": "}",
            "[": "]"

        }
        for char in s:
            if char in parentheses:
                stack.append(char)
            elif char in parentheses.values():
                if len(stack) == 0:
                    return False
                else:
                    x = stack.pop()
                    if parentheses[x] == char:
                        continue
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False


solution = Solution()

print(solution.isValid("[{()}]")
      )
