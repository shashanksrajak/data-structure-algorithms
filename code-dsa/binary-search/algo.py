import time

# decorator function


def time_it(fx):
    def func(*args, **kwargs):
        start_time = time.perf_counter()
        result = fx(*args, **kwargs)
        end_time = time.perf_counter()
        print("Time taken to run the function",
              (end_time-start_time)*1000, "ms")
        return result
    return func


@time_it
def linear_search(nums, search):
    # This takes O(n) time
    for index, num in enumerate(nums):
        if (num == search):
            return index

    return -1


@time_it
def binary_search(nums, search):
    left = 0
    right = len(nums) - 1
    middle = 0

    while left <= right:
        middle = (left + right) // 2   # // gives int quotient
        if (nums[middle] == search):
            return middle
        elif nums[middle] > search:
            right = middle - 1
        else:
            left = middle + 1

    return -1


if __name__ == "__main__":
    # sorted array
    numbers_list = list(range(1, 100001))

    search = 6000

    bs_result = binary_search(numbers_list, search)
    print(f"Number found at index {bs_result} using binary search")

    ls_result = linear_search(numbers_list, search)
    print(f"Number found at index {ls_result} using linear search")
