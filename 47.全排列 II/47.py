#
# @lc app=leetcode.cn id=47 lang=python3
# @lcpr version=
#
# [47] 全排列 II
#
# https://leetcode.cn/problems/permutations-ii/description/
#
# algorithms
# Medium (66.68%)
# Likes:    1711
# Dislikes: 0
# Total Accepted:    658.8K
# Total Submissions: 987.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
#
#
#
# 示例 1：
#
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
# ⁠[1,2,1],
# ⁠[2,1,1]]
#
#
# 示例 2：
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 8
# -10 <= nums[i] <= 10
#
#
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        track = []
        self.backtrack(nums, used, track)
        return self.res

    def backtrack(self, nums: List[int], used: List[bool], track: List[int]):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return
        for i, v in enumerate(nums):
            if used[i]:
                continue
            # 不是第一个没有使用过的数字
            if i > 0 and v == nums[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            track.append(v)
            self.backtrack(nums, used, track)
            used[i] = False
            track.pop()


# @lc code=end


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
