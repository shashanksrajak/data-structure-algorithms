# Source: https://neetcode.io/problems/reorder-linked-list?list=blind75
# https://leetcode.com/problems/reorder-list/
# Difficulty: Easy
# Topic: LinkedList
# Tags: tag1, tag2
# Related Concepts: ..
# Question: ..


def re_order(a: list):

    n = len(a)

    # 0, n-1, 1, n-2
    j = 0  # increment
    k = n-1  # decrement

    b = []
    for i in range(n):
        if i % 2 == 0:
            b.append(a[j])
            j = j+1

        else:
            b.append(a[k])
            k = k-1

    return b


if __name__ == "__main__":
    a = [0, 1, 2, 3, 4, 5, 6]

    print(re_order(a))
