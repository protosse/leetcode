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
