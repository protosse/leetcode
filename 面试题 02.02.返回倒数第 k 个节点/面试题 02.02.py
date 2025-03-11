#
# @lc app=leetcode.cn id=面试题 02.02 lang=python3
# @lcpr version=30101
#
# [面试题 02.02] 返回倒数第 k 个节点
#
# https://leetcode.cn/problems/kth-node-from-end-of-list-lcci/description/
#
# LCCI
# Easy (77.06%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    116.8K
# Total Submissions: 151.6K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
#
# 注意：本题相对原题稍作改动
#
# 示例：
#
# 输入： 1->2->3->4->5 和 k = 2
# 输出： 4
#
# 说明：
#
# 给定的 k 保证是有效的。
#
#

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        if not head:
            return -1
        p1 = head
        for i in range(k):
            p1 = p1.next
        p2 = head
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2.val


# @lc code=end


#
# @lcpr case=start
# 2\n
# @lcpr case=end

#
