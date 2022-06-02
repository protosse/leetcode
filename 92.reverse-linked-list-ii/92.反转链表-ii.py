#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode.cn/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (55.34%)
# Likes:    1304
# Dislikes: 0
# Total Accepted:    300.1K
# Total Submissions: 542.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left  。请你反转从位置 left 到位置 right 的链表节点，返回
# 反转后的链表 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目为 n
# 1 
# -500 
# 1 
# 
# 
# 
# 
# 进阶： 你可以使用一趟扫描完成反转吗？
# 
#

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
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n == 1:
            return head
        last = self.reverseN(head.next, n-1)
        head_next = head.next
        head.next = head_next.next
        head_next.next = head
        return last

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseBetween_iter(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head

        dummyNode = ListNode()
        dummyNode.next = head
        pre = dummyNode

        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        last = None
        for _ in range(right - left + 1):
            next = cur.next
            cur.next = last 
            last = cur
            cur = next

        pre.next.next = cur
        pre.next = last

        return dummyNode.next

# @lc code=end

