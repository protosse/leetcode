from typing import *


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class DoubleNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.pre = None


def head_insert(arr: List[int]) -> Node:
    head = Node()
    for v in arr:
        p = Node(v)
        p.next = head.next
        head.next = p
    return head.next


def tail_insert(arr: List[int]) -> Node:
    head = Node()
    n = head
    for v in arr:
        p = Node(v)
        n.next = p
        n = p
    return head.next


def reverse_list(head: Node) -> Node:
    n = head
    pre: Optional[Node] = None
    while n is not None:
        next = n.next
        n.next = pre
        pre = n
        n = next
    return pre


def reverse_double_list(head: DoubleNode) -> DoubleNode:
    n = head
    pre = None
    while n is not None:
        next = n.next
        n.next = pre
        n.pre = next
        pre = n
        n = next
    return pre


def print_ist(node):
    while node:
        print(node.val)
        node = node.next


add = 0
def add_two_numbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    global add
    if l1 is None and l2 is None and add == 0:
        return None
    v1 = l1.val if l1 else 0
    v2 = l2.val if l2 else 0
    val = v1 + v2 + add
    add = val // 10
    val = val % 10
    node = Node(val)
    node.next = add_two_numbers(l1.next if l1 else None, l2.next if l2 else None)
    return node


if __name__ == '__main__':
    # node = head_insert([1, 2, 3, 4, 5, 6])
    # print_ist(node)
    # node = tail_insert([1, 2, 3, 4, 5, 6])
    # print_ist(node)
    # node = reverse_list(node)
    # print_ist(node)

    # node1 = DoubleNode(1)
    # node2 = DoubleNode(2)
    # node3 = DoubleNode(3)
    # node1.next = node2
    # node2.pre = node1
    # node2.next = node3
    # node3.pre = node2
    # reverse_double_list(node1)
    # print_ist(node3)

    node1 = tail_insert([1, 2, 3])
    node2 = tail_insert([1, 2, 9])
    res_node = add_two_numbers(node1, node2)
    print_ist(res_node)
