# Source: EPI 8.1
# Difficulty: Easy
# Topic: Stacks
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..
"""
Build a Stack ADT with a max() function that returns the max value in stack.

While having a separate variable max is okay, but on pop() it wont work.
So we use caching, we trade time with space.
"""

"""
The solution works in T: O(1) and S: O(n)
"""


import collections
class Stack:
    _cached_items = collections.namedtuple(
        "ElementWithCachedMax", ('element', 'max'))

    def __init__(self):
        self.top = -1
        self.height = 0
        self.items = []

    def max(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1].max

    def push(self, data):
        # this line is the significant line for max
        new_stack_member = self._cached_items(
            data, data if self.is_empty() else max(data, self.max()))

        self.items.append(new_stack_member)
        self.height += 1
        self.top += 1

    def pop(self):
        x = None
        if self.height > 0:
            self.height -= 1
            self.top -= 1
            x = self.items.pop()
        return x

    def print(self):
        for i in range(self.height):
            print(self.items[i])

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.items[-1]

    def is_empty(self):
        return False if self.height != 0 else True

    def __repr__(self):
        return f"Stack(\n  top:{self.top},\n  height:{self.height}\n  items: {self.items}\n)"


if __name__ == "__main__":
    stack = Stack()

    nums = [14, 12, 3, 90, 8, 66, 24]

    print(nums)

    for num in nums:
        stack.push(num)

    print(stack)

    print("Max value is", stack.max())
