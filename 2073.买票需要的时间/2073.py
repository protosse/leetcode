#
# @lc app=leetcode.cn id=2073 lang=python3
# @lcpr version=30008
#
# [2073] 买票需要的时间
#
# https://leetcode.cn/problems/time-needed-to-buy-tickets/description/
#
# algorithms
# Easy (69.79%)
# Likes:    77
# Dislikes: 0
# Total Accepted:    37.8K
# Total Submissions: 54.2K
# Testcase Example:  '[2,3,2]\n2'
#
# 有 n 个人前来排队买票，其中第 0 人站在队伍 最前方 ，第 (n - 1) 人站在队伍 最后方 。
#
# 给你一个下标从 0 开始的整数数组 tickets ，数组长度为 n ，其中第 i 人想要购买的票数为 tickets[i] 。
#
# 每个人买票都需要用掉 恰好 1 秒 。一个人 一次只能买一张票 ，如果需要购买更多票，他必须走到  队尾 重新排队（瞬间
# 发生，不计时间）。如果一个人没有剩下需要买的票，那他将会 离开 队伍。
#
# 返回位于位置 k（下标从 0 开始）的人完成买票需要的时间（以秒为单位）。
#
#
#
# 示例 1：
#
#
# 输入：tickets = [2,3,2], k = 2
#
# 输出：6
#
# 解释：
#
#
# 队伍一开始为 [2,3,2]，第 k 个人以下划线标识。
# 在最前面的人买完票后，队伍在第 1 秒变成 [3,2,1]。
# 继续这个过程，队伍在第 2 秒变为[2,1,2]。
# 继续这个过程，队伍在第 3 秒变为[1,2,1]。
# 继续这个过程，队伍在第 4 秒变为[2,1]。
# 继续这个过程，队伍在第 5 秒变为[1,1]。
# 继续这个过程，队伍在第 6 秒变为[1]。第 k 个人完成买票，所以返回 6。
#
#
#
# 示例 2：
#
#
# 输入：tickets = [5,1,1,1], k = 0
#
# 输出：8
#
# 解释：
#
#
# 队伍一开始为 [5,1,1,1]，第 k 个人以下划线标识。
# 在最前面的人买完票后，队伍在第 1 秒变成 [1,1,1,4]。
# 继续这个过程 3 秒，队伍在第 4 秒变为[4]。
# 继续这个过程 4 秒，队伍在第 8 秒变为[]。第 k 个人完成买票，所以返回 8。
#
#
#
#
#
# 提示：
#
#
# n == tickets.length
# 1 <= n <= 100
# 1 <= tickets[i] <= 100
# 0 <= k < n
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = [i for i in range(len(tickets))]

        second = 0
        while queue:
            second += 1
            # 队头的人买票
            front = queue.pop(0)
            tickets[front] -= 1
            leftTicket = tickets[front]

            # 如果是第k个人且票买完了，直接返回
            if front == k and leftTicket == 0:
                return second
            # 买完了就继续下一个人
            if leftTicket == 0:
                continue
            # 没买完就回到队尾
            queue.append(front)
        return second


# @lc code=end


#
# @lcpr case=start
# [2,3,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [5,1,1,1]\n0\n
# @lcpr case=end

#
