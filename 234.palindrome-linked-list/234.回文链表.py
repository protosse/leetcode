#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode.cn/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (51.61%)
# Likes:    1405
# Dislikes: 0
# Total Accepted:    442.3K
# Total Submissions: 855.8K
# Testcase Example:  '[1,2,2,1]'
#
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,2,1]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围[1, 10^5] 内
# 0 <= Node.val <= 9
# 
# 
# 
# 
# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
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
    def isPalindrome_reverse(self, head: ListNode) -> bool:
        pre = None
        cur = ListNode(head.val, head.next)
        while cur:
            next = cur.next
            new_next = None
            if next:
                new_next = ListNode(next.val, next.next)
            cur.next = pre
            pre = cur
            cur = new_next
        
        p = head
        while pre.next or p.next:
            if pre.val != p.val:
                return False
            pre = pre.next
            p = p.next
        return True

    def isPalindrome(self, head: ListNode) -> bool:
        pass
                    
# @lc code=end

