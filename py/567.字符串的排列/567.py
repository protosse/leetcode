#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=
#
# [567] 字符串的排列
#
# https://leetcode.cn/problems/permutation-in-string/description/
#
# algorithms
# Medium (45.67%)
# Likes:    1050
# Dislikes: 0
# Total Accepted:    318.6K
# Total Submissions: 695.5K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的 排列。如果是，返回 true ；否则，返回 false 。
#
# 换句话说，s1 的排列之一是 s2 的 子串 。
#
#
#
# 示例 1：
#
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#
#
# 示例 2：
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
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, need = {}, {}
        for c in s1:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        valid = 0
        while right < len(s2):
            c = s2[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(s1):
                if valid == len(need):
                    return True
                c = s2[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] = window.get(c, 0) - 1
        return False


# @lc code=end


#
# @lcpr case=start
# "eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "eidboaoo"\n
# @lcpr case=end

#
