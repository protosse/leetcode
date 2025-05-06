#
# @lc app=leetcode.cn id=216 lang=python3
# @lcpr version=
#
# [216] 组合总和 III
#
# https://leetcode.cn/problems/combination-sum-iii/description/
#
# algorithms
# Medium (71.55%)
# Likes:    934
# Dislikes: 0
# Total Accepted:    481.7K
# Total Submissions: 673.2K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#
#
# 只使用数字1到9
# 每个数字 最多使用一次
#
#
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
#
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
# 解释:
# 1 + 2 + 4 = 7
# 没有其他符合的组合了。
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
# 解释:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# 没有其他符合的组合了。
#
# 示例 3:
#
# 输入: k = 4, n = 1
# 输出: []
# 解释: 不存在有效的组合。
# 在[1,9]范围内使用4个不同的数字，我们可以得到的最小和是1+2+3+4 = 10，因为10 > 1，没有有效的组合。
#
#
#
#
# 提示:
#
#
# 2 <= k <= 9
# 1 <= n <= 60
#
#
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(k, n)
        return self.res

    def backtrack(self, k: int, n: int, track: List[int] = None, begin=1):
        if track is None:
            track = []
        if k == 0 and n == 0:
            self.res.append(track.copy())
            return
        for v in range(begin, 10):
            if n - v < 0:
                break
            track.append(v)
            self.backtrack(k - 1, n - v, track, v + 1)
            track.pop()


# @lc code=end


#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n9\n
# @lcpr case=end

# @lcpr case=start
# 4\n1\n
# @lcpr case=end

#
