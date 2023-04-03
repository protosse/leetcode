def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


if __name__ == "__main__":
    arr = [3, 5, 2, 1, 4, 6, 7, 8, 9, 10]
    selectionSort(arr)
    print(arr)
