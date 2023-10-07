def less_index(arr):
    n = len(arr)
    if n == 0:
        return -1
    if n == 1 or arr[0] < arr[1]:
        return 0
    if arr[n - 1] < arr[n - 2]:
        return n - 1
    left = 1
    right = n - 2
    mid = 0
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid - 1]:
            right = mid - 1
        elif arr[mid] > arr[mid + 1]:
            left = mid + 1
        else:
            return mid
    return left


if __name__ == '__main__':
    print(less_index([9,2,1,3,2,4]))
