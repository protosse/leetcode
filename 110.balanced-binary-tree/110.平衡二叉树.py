#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (57.53%)
# Likes:    1315
# Dislikes: 0
# Total Accepted:    494.3K
# Total Submissions: 859.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在范围 [0, 5000] 内
# -10^4 
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
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1
    
    def process(self, root: Optional[TreeNode]) -> Tuple[bool, int]:
        if not root:
            return (True, 0)
        l = self.process(root.left)
        r = self.process(root.right)

        height = max(l[1], r[1]) + 1
        is_balance = l[0] and r[0] and abs(l[1] - r[1]) <= 1

        return (is_balance, height)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        # return self.process(root)[0]
# @lc code=end

