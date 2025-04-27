#
# @lc app=leetcode.cn id=752 lang=python3
# @lcpr version=
#
# [752] 打开转盘锁
#
# https://leetcode.cn/problems/open-the-lock/description/
#
# algorithms
# Medium (53.01%)
# Likes:    692
# Dislikes: 0
# Total Accepted:    141.6K
# Total Submissions: 267.1K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
#
#
#
# 示例 1:
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
#
#
# 示例 2:
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
#
#
# 示例 3:
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
#
#
#
#
# 提示：
#
#
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
#
#
#


# @lc code=start

from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        visited = set()
        step = 0
        q = deque()
        q.append("0000")
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == target:
                    return step
                for s in self.getNeighbors(cur):
                    # 这里的 visited 和 deadends 最好都用set，set判断in的时间复杂度是O(1)
                    # 如果是list的话会超时
                    if s not in visited and s not in dead:
                        q.append(s)
                        visited.add(s)
            step += 1
        return -1

    def plusOne(self, s: str, i: int) -> str:
        """在第i位上加1，即向上拨动第i位"""
        chrs = list(s)
        chr = chrs[i]
        res = int(chr) + 1
        chrs[i] = str(res % 10)
        return "".join(chrs)

    def minusOne(self, s: str, i: int) -> str:
        """在第i位上减1，即向下拨动第i位"""
        chrs = list(s)
        chr = chrs[i]
        res = int(chr) - 1
        chrs[i] = str(9 if res < 0 else res)
        return "".join(chrs)

    def getNeighbors(self, s: str) -> List[str]:
        """拨动s上任意一位后的所有结果
        s一共4位，每一位都可以分别上下拨动一次，故共2x4=8种结果
        """
        res = []
        for i in range(4):
            res.append(self.plusOne(s, i))
            res.append(self.minusOne(s, i))
        return res


# @lc code=end


#
# @lcpr case=start
# ["0201","0101","0102","1212","2002"]\n"0202"\n
# @lcpr case=end

# @lcpr case=start
# ["8888"]\n"0009"\n
# @lcpr case=end

# @lcpr case=start
# ["8887","8889","8878","8898","8788","8988","7888","9888"]\n"8888"\n
# @lcpr case=end

#
