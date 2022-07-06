#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.99%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    202.2K
# Total Submissions: 459.2K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。
# 
# 换句话说，s1 的排列之一是 s2 的 子串 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length, s2.length <= 10^4
# s1 和 s2 仅包含小写字母
# 
# 
#

# @lc code=start

from operator import le
from typing import Dict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need: Dict[str, int] = {}
        window: Dict[str, int] = {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        left, right, valid = 0, 0, 0

        while right < len(s2):
            # c是要移入窗口的字符
            c = s2[right]
            # 右移窗口
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while right - left >= len(s1):
                # 判断是否找到了合法的子串
                if valid == len(need):
                    return True

                # d是要移出窗口的字符
                d = s2[left]
                # 左移窗口
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return False
# @lc code=end

