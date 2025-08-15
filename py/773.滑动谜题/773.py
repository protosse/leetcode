#
# @lc app=leetcode.cn id=773 lang=python3
# @lcpr version=
#
# [773] 滑动谜题
#
# https://leetcode.cn/problems/sliding-puzzle/description/
#
# algorithms
# Hard (70.62%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    42.3K
# Total Submissions: 59.8K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# 在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。一次 移动 定义为选择 0
# 与一个相邻的数字（上下左右）进行交换.
#
# 最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。
#
# 给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。
#
#
#
# 示例 1：
#
#
#
# 输入：board = [[1,2,3],[4,0,5]]
# 输出：1
# 解释：交换 0 和 5 ，1 步完成
#
#
# 示例 2:
#
#
#
# 输入：board = [[1,2,3],[5,4,0]]
# 输出：-1
# 解释：没有办法完成谜板
#
#
# 示例 3:
#
#
#
# 输入：board = [[4,1,2],[5,0,3]]
# 输出：5
# 解释：
# 最少完成谜板的最少移动次数是 5 ，
# 一种移动路径:
# 尚未移动: [[4,1,2],[5,0,3]]
# 移动 1 次: [[4,1,2],[0,5,3]]
# 移动 2 次: [[0,1,2],[4,5,3]]
# 移动 3 次: [[1,0,2],[4,5,3]]
# 移动 4 次: [[1,2,0],[4,5,3]]
# 移动 5 次: [[1,2,3],[4,5,0]]
#
#
#
#
# 提示：
#
#
# board.length == 2
# board[i].length == 3
# 0 <= board[i][j] <= 5
# board[i][j] 中每个值都 不同
#
#
#

# @lc code=start
from typing import List
from collections import deque


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # [0,1,2]
        # [3,4,5]
        target = "123450"
        mapping = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4],
        ]
        start = ""
        for i in board:
            for j in i:
                start += str(j)
        q = deque()
        visited = set()
        q.append(start)
        visited.add(start)
        step = 0
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return step
                idx = cur.index("0")
                for i in mapping[idx]:
                    chars = list(cur)
                    chars[idx], chars[i] = chars[i], chars[idx]
                    ner = "".join(chars)
                    if ner not in visited:
                        q.append(ner)
                        visited.add(ner)
            step += 1
        return -1


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,0,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[5,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,1,2],[5,0,3]]\n
# @lcpr case=end

#
