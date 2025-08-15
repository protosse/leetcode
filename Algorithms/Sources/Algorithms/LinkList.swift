import Foundation

public class ListNode {
    public var val: Int
    public var next: ListNode?
    public init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

// Helper function to create a linked list from an array
public func createLinkedList(_ values: [Int]) -> ListNode? {
    guard !values.isEmpty else { return nil }
    let head = ListNode(values[0])
    var current = head
    for value in values.dropFirst() {
        current.next = ListNode(value)
        current = current.next!
    }
    return head
}

// Helper function to convert a linked list to an array
public func linkedListToArray(_ node: ListNode?) -> [Int] {
    var result: [Int] = []
    var current = node
    while let n = current {
        result.append(n.val)
        current = n.next
    }
    return result
}

/// 21.合并两个有序链表
func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
    guard let list1, let list2 else {
        return list1 == nil ? list2 : list1
    }
    
    let dummy = ListNode()
    var cur: ListNode? = dummy
    var p: ListNode? = list1
    var q: ListNode? = list2
    
    while p != nil && q != nil {
        if p!.val < q!.val {
            cur?.next = p
            p = p?.next
        } else {
            cur?.next = q
            q = q?.next
        }
        cur = cur?.next
    }
    
    cur?.next = p == nil ? q : p
    return dummy.next
}

/// 206.反转链表
func reverseList(_ head: ListNode?) -> ListNode? {
    guard let head else {
        return nil
    }
}
