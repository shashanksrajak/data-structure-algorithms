def partition(items, low, high):
    pivot = items[low]  # select a pivot

    i = low + 1
    j = high

    while i <= j:  # <= makes difference, for 2 elements sorting.
        while i <= high and items[i] <= pivot:  # remember the boundary check
            i += 1
        while j >= low and items[j] > pivot:  # remember the boundary check
            j -= 1

        if i < j:
            # swap the elements
            items[i], items[j] = items[j], items[i]

    # swap the pivot to its right position i.e. with pos of j because that has stopped at the low element
    items[j], items[low] = items[low], items[j]

    # return partition index
    return j


def quick_sort(A, low, high):
    if low < high:
        partition_index = partition(A, low, high)

        # recursive calls
        quick_sort(A, low, partition_index-1)
        quick_sort(A, partition_index+1, high)


A = [2, 4, 6, 8, 10, 12]
B = [21, 4, 12, 4, 12, 18, 9, 2]


print("Original Array", B)

# quick_sort(A, 0, len(A)-1)

quick_sort(B, 0, len(B)-1)

print("Sorted array", B)
