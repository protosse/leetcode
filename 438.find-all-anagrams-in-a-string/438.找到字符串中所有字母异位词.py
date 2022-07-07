#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (54.64%)
# Likes:    935
# Dislikes: 0
# Total Accepted:    201.3K
# Total Submissions: 368.4K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 
# 异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length, p.length <= 3 * 10^4
# s 和 p 仅包含小写字母
# 
# 
#

from typing import List

# @lc code=start
from typing import Dict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need: Dict[str, int] = {}
        window: Dict[str, int] = {}
        for c in p:
            need[c] = need.get(c, 0) + 1
        left, right, valid = 0, 0, 0

        result = []
        while right < len(s):
            # c是要移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            # 判断左侧窗口是否要收缩
            while right - left >= len(p):
                # 判断是否找到了合法的子串
                if valid == len(need):
                    result.append(left)

                # d是要移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return result
# @lc code=end

