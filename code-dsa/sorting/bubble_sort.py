def bubble_sort(arr):
    print("Sorted arr")

    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[i]
                arr[i] = arr[j+1]
                arr[j+1] = temp
    print(arr)


if __name__ == "__main__":
    arr = [3, 1, 9, 4, 8, 0, 5]
    bubble_sort(arr)
