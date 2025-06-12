"""
Quick Sort Algorithm

O(nlogn)
"""


def quicksort(array):
    # base case
    if len(array) < 2:  # in this case the array is already sorted. its a single element so why not!
        return array

    else:
        # select a pivot
        pivot = array[0]

        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]

        # sorting recursion
        return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == "__main__":
    array = [2, 56, 0, 13, 43, 9, 8, 12]
    sorted_array = quicksort(array)
    print("sorted array is: ", sorted_array)
