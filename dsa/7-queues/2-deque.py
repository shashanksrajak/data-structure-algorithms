"""
In Python we have collections library which has deque which is double ended queue

https://docs.python.org/3/library/collections.html
"""

from collections import deque

nums = [12, 32, 44, 56, 19, 21]
d = deque(nums)

print(d.popleft())

d.append(1222)

print(d)
