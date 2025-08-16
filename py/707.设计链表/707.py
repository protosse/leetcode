#
# @lc app=leetcode.cn id=707 lang=python3
# @lcpr version=30008
#
# [707] 设计链表
#
# https://leetcode.cn/problems/design-linked-list/description/
#
# algorithms
# Medium (34.66%)
# Likes:    1112
# Dislikes: 0
# Total Accepted:    374.1K
# Total Submissions: 1.1M
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n' + '[[],[1],[3],[1,2],[1],[1],[1]]'
#
# 你可以选择使用单链表或者双链表，设计并实现自己的链表。
#
# 单链表中的节点应该具备两个属性：val 和 next 。val 是当前节点的值，next 是指向下一个节点的指针/引用。
#
# 如果是双向链表，则还需要属性 prev 以指示链表中的上一个节点。假设链表中的所有节点下标从 0 开始。
#
# 实现 MyLinkedList 类：
#
#
# MyLinkedList() 初始化 MyLinkedList 对象。
# int get(int index) 获取链表中下标为 index 的节点的值。如果下标无效，则返回 -1 。
# void addAtHead(int val) 将一个值为 val 的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
# void addAtTail(int val) 将一个值为 val 的节点追加到链表中作为链表的最后一个元素。
# void addAtIndex(int index, int val) 将一个值为 val 的节点插入到链表中下标为 index 的节点之前。如果
# index 等于链表的长度，那么该节点会被追加到链表的末尾。如果 index 比长度更大，该节点将 不会插入 到链表中。
# void deleteAtIndex(int index) 如果下标有效，则删除链表中下标为 index 的节点。
#
#
#
#
# 示例：
#
# 输入
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# 输出
# [null, null, null, null, 2, null, 3]
#
# 解释
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
# myLinkedList.get(1);              // 返回 2
# myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
# myLinkedList.get(1);              // 返回 3
#
#
#
#
# 提示：
#
#
# 0 <= index, val <= 1000
# 请不要使用内置的 LinkedList 库。
# 调用 get、addAtHead、addAtTail、addAtIndex 和 deleteAtIndex 的次数不超过 2000 。
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

from typing import Optional, Self


class MyLinkedList:

    class Node:
        def __init__(self, val=None):
            self.val = val
            self.next: Self = None
            self.pre: Self = None

    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get_node(self, index) -> Optional[Node]:
        isValid = 0 <= index < self.size
        if not isValid:
            return None
        if index > self.size // 2:
            p = self.tail.pre
            for _ in range(self.size - index - 1):
                p = p.pre
            return p
        else:
            p = self.head.next
            for _ in range(index):
                p = p.next
            return p

    def get(self, index: int) -> int:
        node = self.get_node(index)
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        node = self.Node(val)
        temp = self.head.next
        temp.pre = node
        node.next = temp
        node.pre = self.head
        self.head.next = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.Node(val)
        temp = self.tail.pre
        temp.next = node
        node.pre = temp
        node.next = self.tail
        self.tail.pre = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            p = self.get_node(index)
            if p:
                node = self.Node(val)
                temp = p.pre
                p.pre = node
                node.next = p
                node.pre = temp
                temp.next = node
                self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        p = self.get_node(index)
        if p:
            pre = p.pre
            pre.next = p.next
            p.next.pre = pre
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
