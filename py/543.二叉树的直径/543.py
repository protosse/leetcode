#
# @lc app=leetcode.cn id=543 lang=python3
# @lcpr version=
#
# [543] 二叉树的直径
#
# https://leetcode.cn/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (62.63%)
# Likes:    1716
# Dislikes: 0
# Total Accepted:    586.1K
# Total Submissions: 935.5K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给你一棵二叉树的根节点，返回该树的 直径 。
#
# 二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
#
# 两节点之间路径的 长度 由它们之间边数表示。
#
#
#
# 示例 1：
#
# 输入：root = [1,2,3,4,5]
# 输出：3
# 解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
#
#
# 示例 2：
#
# 输入：root = [1,2]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 10^4] 内
# -100 <= Node.val <= 100
#
#
#

# @lc code=start
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 其实就是二叉树中一个节点的左右子树的最大深度之和
        self.traverse(root)
        return self.res

    def traverse(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)

        self.res = max(self.res, left + right)
        return 1 + max(left, right)


# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#
