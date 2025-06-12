def count_sort(items):
    # python has max() function, but we can also write our own esp in C
    max_number = max(items)

    # create a count array
    # this will add to space complexity for huge range in items
    counter_list = [0] * (max_number+1)

    # store counts
    for item in items:
        counter_list[item] += 1

    # copying back to items from counter
    j = 0  # pointer to counter_list
    i = 0  # pointer to items
    while j < len(counter_list):
        if counter_list[j] > 0:
            items[i] = j
            counter_list[j] -= 1
            i += 1
        else:
            j += 1


if __name__ == "__main__":
    nums = [5, 2, 7, 8, 3, 10, 9, 5, 1]
    count_sort(nums)

    print(nums)
