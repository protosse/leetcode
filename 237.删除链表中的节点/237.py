#
# @lc app=leetcode.cn id=237 lang=python3
# @lcpr version=
#
# [237] 删除链表中的节点
#
# https://leetcode.cn/problems/delete-node-in-a-linked-list/description/
#
# algorithms
# Medium (86.78%)
# Likes:    1404
# Dislikes: 0
# Total Accepted:    402.6K
# Total Submissions: 463.8K
# Testcase Example:  '[4,5,1,9]\n5'
#
# 有一个单链表的 head，我们想删除它其中的一个节点 node。
#
# 给你一个需要删除的节点 node 。你将 无法访问 第一个节点  head。
#
# 链表的所有值都是 唯一的，并且保证给定的节点 node 不是链表中的最后一个节点。
#
# 删除给定的节点。注意，删除节点并不是指从内存中删除它。这里的意思是：
#
#
# 给定节点的值不应该存在于链表中。
# 链表中的节点数应该减少 1。
# node 前面的所有值顺序相同。
# node 后面的所有值顺序相同。
#
#
# 自定义测试：
#
#
# 对于输入，你应该提供整个链表 head 和要给出的节点 node。node 不应该是链表的最后一个节点，而应该是链表中的一个实际节点。
# 我们将构建链表，并将节点传递给你的函数。
# 输出将是调用你函数后的整个链表。
#
#
#
#
# 示例 1：
#
# 输入：head = [4,5,1,9], node = 5
# 输出：[4,1,9]
# 解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9
#
#
# 示例 2：
#
# 输入：head = [4,5,1,9], node = 1
# 输出：[4,5,9]
# 解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [2, 1000]
# -1000 <= Node.val <= 1000
# 链表中每个节点的值都是 唯一 的
# 需要删除的节点 node 是 链表中的节点 ，且 不是末尾节点
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


# @lc code=end


#
# @lcpr case=start
# [4,5,1,9]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,5,1,9]\n1\n
# @lcpr case=end

#
