#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (44.34%)
# Likes:    1961
# Dislikes: 0
# Total Accepted:    306.1K
# Total Submissions: 689.6K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
# 示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# 1
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
import sys
from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need: Dict[str, int] = {}
        window: Dict[str, int] = {}

        for c in t:
            need[c] = need.get(c, 0) + 1

        left, right, valid = 0, 0, 0
        # start记录最小覆盖子串的起始索引
        # length记录其长度
        start = 0
        length = sys.maxsize

        while right < len(s):
            # c是要移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1

            # 更新窗口数据
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否需要收缩
            while valid == len(need):
                # 记录最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left
                # d是要移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 更新窗口数据
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return '' if length == sys.maxsize else s[start:start+length]
# @lc code=end