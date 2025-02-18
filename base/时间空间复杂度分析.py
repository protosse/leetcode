def getSum(nums: list[int]) -> int:
    """计算数组中所有元素的和

    Args:
        nums (list[int]): 数组

    Returns:
        int: 数组中所有元素的和
    """
    # 只用了一个sum变量来存储，空间复杂度为O(1)
    sum = 0
    # for循环遍历nums数组，时间复杂度为O(n)，n代表数组的长度
    for n in nums:
        sum += nums[n]
    return sum


def hasTargetSum(nums: list[int], target: int) -> bool:
    """数组是否存在两个数，它们的和为 target

    Args:
        nums (list[int]): 数组
        target (int): 目标和
    """
    # 嵌套了两层for循环，时间复杂度为O(n^2)
    # 只使用了两个变量i，j，这是常数级别的空间消耗，空间复杂度为O(1)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False


def squareArray(nums: list[int]) -> list[int]:
    """返回数组中每个元素的平方

    Args:
        nums (list[int]): 数组

    Returns:
        list[int]: 数组中每个元素的平方
    """
    # 创建了一个新的数组，空间复杂度为O(n)
    # for循环遍历nums数组，时间复杂度为O(n)
    return [n**2 for n in nums]


def quickSort(nums: list[int]) -> list[int]:
    """快速排序

    Args:
        nums (list[int]): 数组

    Returns:
        list[int]: 排序后数组
    """
    if len(nums) <= 1:
        return nums

    stack = [(0, len(nums) - 1)]

    while stack:
        start, end = stack.pop()
        if start >= end:
            continue

        pivot = nums[start]
        low = start
        high = end

        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]

        nums[low] = pivot

        stack.append((start, low - 1))
        stack.append((low + 1, end))

    return nums
