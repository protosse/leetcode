#
# @lc app=leetcode.cn id=387 lang=python3
# @lcpr version=
#
# [387] 字符串中的第一个唯一字符
#
# https://leetcode.cn/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (57.34%)
# Likes:    776
# Dislikes: 0
# Total Accepted:    462.8K
# Total Submissions: 806.1K
# Testcase Example:  '"leetcode"'
#
# 给定一个字符串 s ，找到 它的第一个不重复的字符，并返回它的索引 。如果不存在，则返回 -1 。
#
#
#
# 示例 1：
#
# 输入: s = "leetcode"
# 输出: 0
#
#
# 示例 2:
#
# 输入: s = "loveleetcode"
# 输出: 2
#
#
# 示例 3:
#
# 输入: s = "aabb"
# 输出: -1
#
#
#
#
# 提示:
#
#
# 1 <= s.length <= 10^5
# s 只包含小写字母
#
#
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        for c in s:
            dict[c] = not c in dict

        for i, c in enumerate(s):
            if dict[c]:
                return i
        return -1


# @lc code=end


#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#
