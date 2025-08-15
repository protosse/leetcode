#
# @lc app=leetcode.cn id=78 lang=python3
# @lcpr version=
#
# [78] 子集
#
# https://leetcode.cn/problems/subsets/description/
#
# algorithms
# Medium (82.25%)
# Likes:    2486
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
#
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#
#
# 示例 2：
#
# 输入：nums = [0]
# 输出：[[],[0]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10
# -10 <= nums[i] <= 10
# nums 中的所有元素 互不相同
#
#
#

# @lc code=start

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums: List[int], start: int, track: List[int]):
        # 任何一个能进入递归的都一定是一个正确的集合
        # 因为源数组每个元素都不相同，并且1只能和2或3组成集合,2只能和3组成集合,3只能和自己，所以进入的一定是唯一的
        self.res.append(track.copy())
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#
