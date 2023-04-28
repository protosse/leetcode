#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (71.33%)
# Likes:    1943
# Dislikes: 0
# Total Accepted:    486.7K
# Total Submissions: 682.4K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
# 
# 
# 示例 2:
# 
# 
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_n = len(preorder)
        in_n = len(inorder)
        if len(preorder) != len(inorder) or pre_n == 0:
            return None
        self.inOrderMap = {}
        for i, v in enumerate(inorder):
            self.inOrderMap[v] = i
        return self.f(preorder, 0, pre_n -1, inorder, 0, in_n - 1)
        
    def f(self, preorder: List[int], l1: int, r1: int, inorder: List[int], l2: int, r2: int) -> Optional[TreeNode]:
        if l1 > r1:
            return None
        head = TreeNode(preorder[l1])
        if l1 == r1:
            return head
        find = self.inOrderMap[preorder[l1]]
        step = find - l2
        head.left = self.f(
            preorder, l1 + 1, l1 + step,
            inorder, l2, find - 1
        )
        head.right = self.f(
            preorder, l1 + step + 1, r1,
            inorder, find + 1, r2
        )
        return head

# @lc code=end

