#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.30%)
# Likes:    723
# Dislikes: 0
# Total Accepted:    123.1K
# Total Submissions: 161.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。
# 
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。
# 
# 
# 
# 示例 1:
# 
# 
# 
# 
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
# 
# 
# 示例 2:
# 
# 
# 输入: head = []
# 输出: []
# 
# 
# 
# 
# 提示:
# 
# 
# head 中的节点数在[0, 2 * 10^4] 范围内
# -10^5 <= Node.val <= 10^5
# 
# 
#

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        pass
# @lc code=end

