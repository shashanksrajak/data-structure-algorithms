"""
Find missing elements in an array.

Leetcode similar question -> https://leetcode.com/problems/missing-number

e.g.
A = [4, 1, 8, 7, 3, 11, 9]

missing elements - 2, 5, 6, 10
"""

"""
If the array is sorted then we can use diff approach
A[i] - i = diff (some constant diff); if not then missing element

-->> but for general case, unsorted array we can implement this method of hashing
Time -> O(n)
Space -> O(n + max_num)
"""


def missing_elements(items):
    # find min and max elements in items
    max_num = max(items)
    # min_num = min(items)

    # create a hash list
    hash_list = [0] * (max_num+1)

    for num in items:
        hash_list[num] += 1

    # if the problem says find missing elements in a range of number then we can just search in low-high

    result = []
    for i in range(1, max_num+1):
        if hash_list[i] == 0:
            result.append(i)

    return result


    # run
items = [4, 1, 8, 7, 3, 11, 9]
result = missing_elements(items)
print("missing elements\n", result)
