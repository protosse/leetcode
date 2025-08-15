#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=
#
# [46] 全排列
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (80.06%)
# Likes:    3091
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# 示例 2：
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
# 示例 3：
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
#
#
#

from typing import List


# @lc code=start
class Solution:

    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res.clear()
        used = [False] * len(nums)
        track = []
        self.backtrack(nums, used, track)
        return self.res

    def backtrack(self, nums: List[int], used: List[bool], track: List[int]):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        for i, num in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            track.append(num)
            self.backtrack(nums, used, track)
            used[i] = False
            track.remove(num)


# @lc code=end


#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
