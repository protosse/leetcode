#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode.cn/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (36.90%)
# Likes:    1998
# Dislikes: 0
# Total Accepted:    709.7K
# Total Submissions: 1.9M
# Testcase Example:  '[2,1,3]'
#
# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
# 
# 有效 二叉搜索树定义如下：
# 
# 
# 节点的左子树只包含 小于 当前节点的数。
# 节点的右子树只包含 大于 当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [2,1,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目范围在[1, 10^4] 内
# -2^31 <= Node.val <= 2^31 - 1
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
    
    def process(self, root: Optional[TreeNode]) -> Optional[Tuple[bool, int, int]]:
        """return info

        Args:
            root (Optional[TreeNode]): node

        Returns:
            Optional[Tuple[bool, int, int]]: isBST, max val, min val
        """
        if not root:
            return None
        l = self.process(root.left)
        r = self.process(root.right)

        max_val = root.val
        min_val = root.val
        if l:
            max_val = max(l[1], max_val)
            min_val = min(l[2], min_val)
        if r:
            max_val = max(r[1], max_val)
            min_val = min(r[2], min_val)
        
        is_bst = True
        # 如果左树不是搜索二叉树，整棵树都不是了
        if l and not l[0]:
            is_bst = False
        # 同理右树
        if r and not r[0]:
            is_bst = False
        
        # 左树的最大值必须小于根节点的值
        left_max_less_root = True if not l else l[1] < root.val
        # 右树的最小值必须大于根节点的值
        right_min_more_root = True if not r else r[2] > root.val

        if not left_max_less_root or not right_min_more_root:
            is_bst = False
        return (is_bst, max_val, min_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.process(root)[0]
        
# @lc code=end

