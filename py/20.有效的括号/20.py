# @before-stub-for-debug-begin
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30008
#
# [20] 有效的括号
#
# https://leetcode.cn/problems/valid-parentheses/description/
#
# algorithms
# Easy (44.51%)
# Likes:    4643
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 4.7M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "()"
#
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "()[]{}"
#
# 输出：true
#
#
# 示例 3：
#
#
# 输入：s = "(]"
#
# 输出：false
#
#
# 示例 4：
#
#
# 输入：s = "([])"
#
# 输出：true
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 仅由括号 '()[]{}' 组成
#
#
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "{([":
                stack.append(c)
            elif stack and self.leftOf(c) == stack[-1]:
                stack.pop()
            else:
                return False
        return not stack

    def leftOf(self, c: str) -> str:
        if c == "}":
            return "{"
        if c == ")":
            return "("
        return "["


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#
