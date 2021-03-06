#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (38.84%)
# Likes:    7780
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 4.7M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 5 * 10^4
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start

from typing import Dict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windows: Dict[str, int] = {}
        left, right = 0, 0
        res = 0

        while right < len(s):
            c = s[right]
            right += 1
            windows[c] = windows.get(c, 0) + 1
            # 当 window[c] 值大于 1 时，说明窗口中存在重复字符，不符合条件，就该移动 left 缩小窗口
            while windows[c] > 1:
                d = s[left]
                left += 1
                windows[d] = windows.get(d, 0) - 1
            # 在此更新最大长度
            res = max(res, right - left)

        return res
        
# @lc code=end

