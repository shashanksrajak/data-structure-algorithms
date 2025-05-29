def bubble_sort(items):
    for i in range(len(items)-1):
        swapped = False
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]  # swap items
                swapped = True
        # in one pass if no swapping, array is sorted
        if not swapped:
            break


if __name__ == "__main__":
    nums = [5, 2, 7, 8, 3]
    nums = [5, 2]

    bubble_sort(nums)
    print(nums)
