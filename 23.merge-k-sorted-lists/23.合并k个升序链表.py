#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (56.95%)
# Likes:    1969
# Dislikes: 0
# Total Accepted:    472.4K
# Total Submissions: 829.5K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 给你一个链表数组，每个链表都已经按升序排列。
# 
# 请你将所有链表合并到一个升序链表中，返回合并后的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
# ⁠ 1->4->5,
# ⁠ 1->3->4,
# ⁠ 2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
# 
# 
# 示例 2：
# 
# 输入：lists = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 输入：lists = [[]]
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# k == lists.length
# 0 <= k <= 10^4
# 0 <= lists[i].length <= 500
# -10^4 <= lists[i][j] <= 10^4
# lists[i] 按 升序 排列
# lists[i].length 的总和不超过 10^4
# 
# 
#

from typing import List, Optional

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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 虚拟头节点
        head = ListNode()
        cur = head
        i = list1
        j = list2

        while i != None and j != None:
            # 比较两个节点的值，将较小的节点接到cur的后面
            if i.val <= j.val:
                cur.next = i
                i = i.next
            else:
                cur.next = j
                j = j.next
                # 不断向前
            cur = cur.next
        # 如果有一个为空了，那么直接将另一个链表接到cur的后面
        cur.next = i if i != None else j
        return head.next

    def merge(self, lists: List[Optional[ListNode]], start, end) -> Optional[ListNode]:
        if start == end:
            return lists[start]
        if start > end:
            return None
        mid = (start + end) // 2
        # can also
        # mid = (start + end) >> 1
        return self.mergeTwoLists(self.merge(lists, start, mid), self.merge(lists, mid + 1, end))

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.merge(lists, 0, len(lists) - 1)

# @lc code=end

