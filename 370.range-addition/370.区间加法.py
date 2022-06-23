#
# @lc app=leetcode.cn id=370 lang=python3
#
# [370] 区间加法
#
# https://leetcode.cn/problems/range-addition/description/
#
#
# 假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k 个更新的操作。
# 其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，
# 你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
# 请你返回 k 次操作后的数组。
#
# 示例:
# 输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# 输出: [-2,0,3,5,3]
#
# 解释:
#
# 初始状态:
# [0,0,0,0,0]
#
# 进行了操作 [1,3,2] 后的状态:
# [0,2,2,2,0]
#
# 进行了操作 [2,4,3] 后的状态:
# [0,2,5,5,3]
#
# 进行了操作 [0,2,-2] 后的状态:
# [-2,0,3,5,3]


from typing import List

# @lc code=start


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]):
        # 初始都是0
        nums = [0 for _ in range(length)]

        # 差分数组初始也是0
        df = [0 for _ in range(length)]

        for update in updates:
            i = update[0]
            j = update[1]
            inc = update[2]

            df[i] += inc
            # 边界判断
            if j+1 < length:
                df[j+1] -= inc

        # 根据差分数组还原数组
        nums[0] = df[0]
        for i in range(1, length):
            nums[i] = nums[i-1] + df[i]
        return nums

# @lc code=end
