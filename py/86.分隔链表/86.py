#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30100
#
# [86] 分隔链表
#
# https://leetcode.cn/problems/partition-list/description/
#
# algorithms
# Medium (65.38%)
# Likes:    892
# Dislikes: 0
# Total Accepted:    333K
# Total Submissions: 508.8K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
#
# 你应当 保留 两个分区中每个节点的初始相对位置。
#
#
#
# 示例 1：
#
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#
#
# 示例 2：
#
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 链表中节点的数目在范围 [0, 200] 内
# -100 <= Node.val <= 100
# -200 <= x <= 200
#
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """把原链表分成两个小链表，
        一个链表中的元素大小都小于 x
        另一个链表中的元素都大于等于 x
        最后再把这两条链表接到一起
        """
        small = ListNode()
        small_tail = small
        big = ListNode()
        big_tail = big
        p = head
        while p:
            if p.val < x:
                small_tail.next = p
                small_tail = p
            else:
                big_tail.next = p
                big_tail = p

            # 不能直接让 p 指针前进，
            # p = p.next
            # 断开原链表中的每个节点的 next 指针
            t = p.next
            p.next = None
            p = t

        small_tail.next = big.next
        return small.next


# @lc code=end

#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#
