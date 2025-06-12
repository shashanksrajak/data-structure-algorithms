def median_of_three(items, low, high):
    """Find median of first, middle, and last elements"""
    mid = (low + high) // 2

    # Get the three values
    first = items[low]
    middle = items[mid]
    last = items[high]

    # Find median and return its index
    if (first <= middle <= last) or (last <= middle <= first):
        return mid
    elif (middle <= first <= last) or (last <= first <= middle):
        return low
    else:
        return high


def partition_median(items, low, high):
    # Find median of three and swap it to the first position
    median_index = median_of_three(items, low, high)
    items[low], items[median_index] = items[median_index], items[low]

    # Now use the same partition logic as before
    pivot = items[low]  # This is now the median element

    i = low + 1
    j = high

    while i <= j:
        while i <= high and items[i] <= pivot:
            i += 1
        while j >= low and items[j] > pivot:
            j -= 1

        if i < j:
            items[i], items[j] = items[j], items[i]

    items[j], items[low] = items[low], items[j]
    return j


def quick_sort_median(A, low, high):
    if low < high:
        partition_index = partition_median(A, low, high)

        quick_sort_median(A, low, partition_index-1)
        quick_sort_median(A, partition_index+1, high)


# Test both versions
A = [2, 4, 6, 8, 10, 12]
B = [21, 4, 12, 4, 12, 18, 9, 2]
C = B.copy()  # Copy for comparison

print("Original Array:", B)

# # Regular quick sort
# quick_sort(B, 0, len(B)-1)
# print("Regular Quick Sort:", B)

# Median-of-three quick sort
quick_sort_median(C, 0, len(C)-1)
print("Median Quick Sort:", C)
