#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (36.69%)
# Likes:    5253
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.8M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def palindrome(self, s: str, left: int, right: int):
        '''
        以 left 和 right 为中心的回文子串
        '''
        while left >= 0 and right< len(s) and s[left] == s[right]:
            # 双指针，向两边扩展
            left -= 1
            right += 1
        return s[left+1:right]

    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            # 以 s[i] 为中心的回文子串
            l = self.palindrome(s, i, i)
            # 以 s[i] 和 s[i+1] 为中心的回文子串
            r = self.palindrome(s, i, i+1)
            res = max(res, l, r, key=len)
        return res

# @lc code=end

