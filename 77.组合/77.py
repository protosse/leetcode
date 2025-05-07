#
# @lc app=leetcode.cn id=77 lang=python3
# @lcpr version=
#
# [77] 组合
#
# https://leetcode.cn/problems/combinations/description/
#
# algorithms
# Medium (77.64%)
# Likes:    1763
# Dislikes: 0
# Total Accepted:    883.8K
# Total Submissions: 1.1M
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。
#
# 你可以按 任何顺序 返回答案。
#
#
#
# 示例 1：
#
# 输入：n = 4, k = 2
# 输出：
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
# 示例 2：
#
# 输入：n = 1, k = 1
# 输出：[[1]]
#
#
#
# 提示：
#
#
# 1 <= n <= 20
# 1 <= k <= n
#
#
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(n, k)
        return self.res

    def backtrack(self, n: int, k: int, start: int = 1, track: List[int] = None):
        if track is None:
            track = []
        if len(track) == k:
            self.res.append(track.copy())
            return
        for i in range(start, n + 1):
            track.append(i)
            self.backtrack(n, k, i + 1, track)
            track.pop()


# @lc code=end


#
# @lcpr case=start
# 4\n2\n
# @lcpr case=end

# @lcpr case=start
# 1\n1\n
# @lcpr case=end

#
