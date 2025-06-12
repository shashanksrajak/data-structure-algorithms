def bubble_sort(arr: list[int]) -> tuple[list[int], int]:
    n = len(arr)
    passes = 0
    arr = arr.copy()  # To avoid modifying the original input

    for i in range(n):
        swapped = False
        # Last i elements are already in place
        ##### Write your code here #######
        j = 0
        while j < n-i-1:
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True
            j = j+1

        passes += 1
        print((arr, passes))
        if not swapped:
            break  # Array is sorted; terminate early

    return arr, passes


print("Final Results: ", bubble_sort([1, 2, 43, 65, 3, 8, 9, 111, 73, 4, 5]))
