def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [3, 2, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(bubbleSort(arr))