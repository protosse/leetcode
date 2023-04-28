#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.23%)
# Likes:    1005
# Dislikes: 0
# Total Accepted:    277K
# Total Submissions: 383.8K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
# 
# 
#

from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        post_n = len(postorder)
        in_n = len(inorder)
        if len(postorder) != len(inorder) or post_n == 0:
            return None
        self.inOrderMap = {}
        for i, v in enumerate(inorder):
            self.inOrderMap[v] = i
        return self.f(inorder, 0, in_n -1, postorder, 0, post_n - 1)

    def f(self, inorder, l1, r1, postorder, l2, r2) -> Optional[TreeNode]:
        if l2 > r2:
            return None
        head = TreeNode(postorder[r2])
        if l2 == r2:
            return head
        find = self.inOrderMap[postorder[r2]]
        step = find - l1
        head.left = self.f(
            inorder, l1, l1 + step - 1,
            postorder, l2, l2 + step - 1
        )
        head.right = self.f(
            inorder, find + 1, r1,
            postorder, l2 + step, r2 - 1
        )
        return head
# @lc code=end

