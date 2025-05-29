# def partition(items, low, high):
#     pivot = low  # it is up to us which pivot we want to choose

#     i = low + 1  # pointer tracking larger elements than pivot
#     j = high  # tracking smaller elements than pivot

#     while i < j:
#         while items[i] <= items[pivot] and i <= high:
#             i = i + 1
#         while items[j] > items[pivot] and j >= low+1:
#             j = j - 1

#         if i < j:
#             items[i], items[j] = items[j], items[i]

#     # we swap pivot with A[j]
#     items[pivot], items[j] = items[j], items[pivot]

#     return j

def partition(items, low, high):
    pivot = items[low]
    i = low + 1
    j = high

    while True:
        while i <= high and items[i] <= pivot:
            i = i + 1
        while j >= low and items[j] > pivot:
            j = j - 1

        if i < j:
            items[i], items[j] = items[j], items[i]
        else:
            break

    items[low], items[j] = items[j], items[low]
    return j


def quick_sort(items, low, high):
    if low < high:
        part_index = partition(items, low, high)
        print(part_index)
        quick_sort(items, low, part_index-1)
        quick_sort(items, part_index+1, high)


if __name__ == "__main__":
    # nums = [5, 2, 7, 8, 3, 10, 9, 5, 1]

    nums = [4, 5]
    quick_sort(nums, 0, len(nums)-1)

    print(nums)
