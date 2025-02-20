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


def partition(nums: list[int], left: int, right: int) -> int:
    """快速排序 分区函数

    Args:
        nums (list[int]): 数组
        left (int): 左
        right (int): 右

    Returns:
        int: left对应num的最终位置
    """
    num = nums[left]
    while left < right:
        while left < right and nums[right] >= num:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= num:
            left += 1
        nums[right] = nums[left]
    nums[left] = num
    return left


def quickSort(nums: list[int], left: int, right: int):
    """快速排序
    时间复杂度为O(nlogn)
    空间复杂度为O(logn)

    Args:
        nums (list[int]): 数组
        left (int): 左
        right (int): 右
    """
    if left < right:
        pi = partition(nums, left, right)
        quickSort(nums, left, pi - 1)
        quickSort(nums, pi + 1, right)
