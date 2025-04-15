#
# @lc app=leetcode.cn id=509 lang=python3
# @lcpr version=
#
# [509] 斐波那契数
#
# https://leetcode.cn/problems/fibonacci-number/description/
#
# algorithms
# Easy (65.87%)
# Likes:    838
# Dislikes: 0
# Total Accepted:    841.5K
# Total Submissions: 1.3M
# Testcase Example:  '2'
#
# 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0，F(1) = 1
# F(n) = F(n - 1) + F(n - 2)，其中 n > 1
#
#
# 给定 n ，请计算 F(n) 。
#
#
#
# 示例 1：
#
# 输入：n = 2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
#
#
# 示例 2：
#
# 输入：n = 3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
#
#
# 示例 3：
#
# 输入：n = 4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
#
#
#
#
# 提示：
#
#
# 0 <= n <= 30
#
#
#


# @lc code=start
class Solution:
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        # if n < 2:
        #     return n
        # if n in self.memo:
        #     return self.memo[n]
        # v = self.fib(n - 1) + self.fib(n - 2)
        # self.memo[n] = v
        # return v

        if n == 0 or n == 1:
            return n
        # 只存 fib - 1 和 fib - 2 的值
        dp_i_1 = 1
        dp_i_2 = 0
        for i in range(2, n + 1):
            dp_i = dp_i_1 + dp_i_2
            # 滚动更新
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i_1


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#
