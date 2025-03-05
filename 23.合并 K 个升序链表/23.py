#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30100
#
# [23] 合并 K 个升序链表
#
# https://leetcode.cn/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (61.15%)
# Likes:    2965
# Dislikes: 0
# Total Accepted:    942.5K
# Total Submissions: 1.5M
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

from typing import Optional, List


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

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        dummy = ListNode()
        cur = dummy
        p = list1
        q = list2
        while p and q:
            if p.val < q.val:
                cur.next = p
                p = p.next
            else:
                cur.next = q
                q = q.next
            cur = cur.next
        cur.next = p if p else q
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(lists, left, right):
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(lists, left, mid)
            l2 = merge(lists, mid + 1, right)
            return self.mergeTwoLists(l1, l2)

        return merge(lists, 0, len(lists) - 1)


# @lc code=end


#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#
