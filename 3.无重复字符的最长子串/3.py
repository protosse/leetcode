#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=
#
# [3] 无重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (40.67%)
# Likes:    10755
# Dislikes: 0
# Total Accepted:    3.4M
# Total Submissions: 8.3M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
#
#
#
# 示例 1:
#
# 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#
#
# 示例 2:
#
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#
#
# 示例 3:
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
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = {}
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1

            while window.get(c) > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            res = max(res, right - left)
        return res


# @lc code=end


#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#
