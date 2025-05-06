#
# @lc app=leetcode.cn id=40 lang=python3
# @lcpr version=
#
# [40] 组合总和 II
#
# https://leetcode.cn/problems/combination-sum-ii/description/
#
# algorithms
# Medium (60.02%)
# Likes:    1678
# Dislikes: 0
# Total Accepted:    627.5K
# Total Submissions: 1M
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用 一次 。
#
# 注意：解集不能包含重复的组合。
#
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 输出:
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 输出:
# [
# [1,2,2],
# [5]
# ]
#
#
#
# 提示:
#
#
# 1 <= candidates.length <= 100
# 1 <= candidates[i] <= 50
# 1 <= target <= 30
#
#
#

# @lc code=start

from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.backtrack(candidates, target)
        return self.res

    def backtrack(
        self,
        candidates: List[int],
        target: int,
        track: List[int] = None,
        begin: int = 0,
    ):
        """我们需要限制相等元素在每一轮中只被选择一次。实现方式比较巧妙：
        由于数组是已排序的，因此相等元素都是相邻的。这意味着在某轮选择中，若当前元素与其左边元素相等，则说明它已经被选择过，因此直接跳过当前元素。
        与此同时，本题规定中的每个数组元素只能被选择一次。
        幸运的是，我们也可以利用变量 start 来满足该约束：当做出选择 xi 后
        设定下一轮从索引 i+1 开始向后遍历。这样即能去除重复子集，也能避免重复选择元素。
        """
        if track is None:
            track = []

        if target == 0:
            self.res.append(track.copy())
            return
        for i in range(begin, len(candidates)):
            candi = candidates[i]
            if target - candi < 0:
                break
            if i > begin and candi == candidates[i - 1]:
                continue
            track.append(candi)
            self.backtrack(candidates, target - candi, track, i + 1)
            track.pop()


# @lc code=end


#
# @lcpr case=start
# [10,1,2,7,6,1,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2,5,2,1,2]\n5\n
# @lcpr case=end

#
