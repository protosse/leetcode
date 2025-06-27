#
# @lc app=leetcode.cn id=242 lang=python3
# @lcpr version=
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (67.35%)
# Likes:    1019
# Dislikes: 0
# Total Accepted:    969.3K
# Total Submissions: 1.4M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
#
#
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母
#
#
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
        for c in t:
            if c in dict:
                if dict[c] == 1:
                    dict.pop(c)
                else:
                    dict[c] -= 1
        return not dict


# @lc code=end


#
# @lcpr case=start
# "anagram"\n"nagaram"\n
# @lcpr case=end

# @lcpr case=start
# "rat"\n"car"\n
# @lcpr case=end

#
