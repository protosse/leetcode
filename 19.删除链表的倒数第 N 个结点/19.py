#
# @lc app=leetcode.cn id=19 lang=python3
# @lcpr version=30101
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (50.22%)
# Likes:    3059
# Dislikes: 0
# Total Accepted:    1.7M
# Total Submissions: 3.3M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#
#
# 示例 1：
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
# 示例 2：
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
# 示例 3：
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
#
#
#
#
# 进阶：你能尝试使用一趟扫描实现吗？
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        h = head
        p1 = head
        for i in range(n):
            if p1:
                p1 = p1.next
        if not p1:
            h = h.next
            return h
        p2 = head
        p2_pre = None
        while p1:
            p1 = p1.next
            p2_pre = p2
            p2 = p2.next
        p2_pre.next = p2.next
        p2.next = None
        return h


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#
