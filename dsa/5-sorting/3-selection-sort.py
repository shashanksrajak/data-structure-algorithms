def selection_sort(items):
    for i in range(len(items)-1):
        k = i
        for j in range(i, len(items)):
            if items[j] < items[k]:
                k = j
        # once this inner for loop is done, we have found the right element to swap (here minimum element)
        items[i], items[k] = items[k], items[i]


if __name__ == "__main__":
    nums = [5, 2, 7, 8, 3, 10, 9, 5, 1]
    selection_sort(items=nums)
    print(nums)
