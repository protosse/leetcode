#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=
#
# [322] 零钱兑换
#
# https://leetcode.cn/problems/coin-change/description/
#
# algorithms
# Medium (50.02%)
# Likes:    3034
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,5]\n11'
#
# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。
#
# 计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
#
# 你可以认为每种硬币的数量是无限的。
#
#
#
# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1
#
# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1
#
# 示例 3：
#
# 输入：coins = [1], amount = 0
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#

from typing import List


# @lc code=start
class Solution:
    def __init__(self):
        self.memo = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.dp2(coins, amount)

    def dp(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        elif amount < 0:
            return -1

        if amount in self.memo:
            return self.memo[amount]

        res = float("inf")
        for coin in coins:
            sub = self.dp(coins, amount - coin)
            if sub == -1:
                continue
            res = min(res, sub + 1)
        self.memo[amount] = res if res != float("inf") else -1
        return self.memo[amount]

    def dp2(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return -1 if dp[amount] == amount + 1 else dp[amount]


# @lc code=end


#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
