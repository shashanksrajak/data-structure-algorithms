def merge_sort(arr: list[int]) -> tuple[list[int], int]:
    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(arr) and j < len(arr):
            if arr[i] < arr[j]:
                merged.append(arr[i])
                i = i+1
            else:
                merged.append(arr[j])
                j = j+1

        merged.extend(arr[i:])
        merged.extend(arr[j:])

        return merged

    def recursive_sort(sub_arr):
        nonlocal merge_count
        if len(sub_arr) <= 1:
            return sub_arr

        mid = len(sub_arr) // 2
        left = recursive_sort(sub_arr[:mid])
        right = recursive_sort(sub_arr[mid:])

        merge_count += 1  # Count each merge operation
        print((sub_arr, merge_count))
        return merge(left, right)

    merge_count = 0
    sorted_arr = recursive_sort(arr)
    return sorted_arr, merge_count


print("Final Results: ", merge_sort([5, 100, 80, 23, 94, 1, 4, 2, 8]))
