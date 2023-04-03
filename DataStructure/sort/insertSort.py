def insertSort(arr):
    for i in range(1, len(arr)):
        cur = i
        while cur > 0 and arr[cur] < arr[cur - 1]:
            arr[cur], arr[cur - 1] = arr[cur - 1], arr[cur]
            cur -= 1
    return arr


if __name__ == "__main__":
    arr = [3, 5, 2, 1, 4, 6, 8, 7, 9, 10]
    print(insertSort(arr))
