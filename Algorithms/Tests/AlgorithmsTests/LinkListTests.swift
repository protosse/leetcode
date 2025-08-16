@testable import Algorithms
import Testing

@Test("21.合并两个有序链表")
func testMergeTwoLists() throws {
    let list1 = createLinkedList([1, 2, 4])
    let list2 = createLinkedList([1, 3, 4])

    let mergedList = mergeTwoLists(list1, list2)

    #expect(linkedListToArray(mergedList) == [1, 1, 2, 3, 4, 4])
}

@Test("206.反转链表")
func testReverseList() throws {
    let list = createLinkedList([1, 2, 3, 4, 5])

    let res = reverseList(list)

    #expect(linkedListToArray(res) == [5, 4, 3, 2, 1])
}
