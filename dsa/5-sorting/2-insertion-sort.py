def insertion_sort(items):
    # assume first element is already sorted and start outer pass from i=1
    for i in range(1, len(items)):
        x = items[i]  # this is the item we need to insert in the left sublist
        j = i-1  # this pointer moves to the left for comparing and shifting

        while (j > -1 and items[j] > x):
            items[j+1] = items[j]
            j -= 1
        items[j+1] = x


if __name__ == "__main__":
    nums = [5, 2, 7, 8, 3, 10, 9, 5, 1]
    insertion_sort(nums)
    print(nums)
