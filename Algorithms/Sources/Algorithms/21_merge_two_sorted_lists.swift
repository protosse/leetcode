/*
 * @lc app=leetcode.cn id=21 lang=swift
 * @lcpr version=30202
 *
 * [21] 合并两个有序链表
 *
 * https://leetcode.cn/problems/merge-two-sorted-lists/description/
 *
 * algorithms
 * Easy (67.98%)
 * Likes:    3833
 * Dislikes: 0
 * Total Accepted:    2.1M
 * Total Submissions: 3.2M
 * Testcase Example:  '[1,2,4]\n[1,3,4]'
 *
 * 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
 *
 *
 *
 * 示例 1：
 *
 * 输入：l1 = [1,2,4], l2 = [1,3,4]
 * 输出：[1,1,2,3,4,4]
 *
 *
 * 示例 2：
 *
 * 输入：l1 = [], l2 = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 * 输入：l1 = [], l2 = [0]
 * 输出：[0]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 两个链表的节点数目范围是 [0, 50]
 * -100 <= Node.val <= 100
 * l1 和 l2 均按 非递减顺序 排列
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public var val: Int
 *     public var next: ListNode?
 *     public init() { self.val = 0; self.next = nil; }
 *     public init(_ val: Int) { self.val = val; self.next = nil; }
 *     public init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next; }
 * }
 */
// class Solution {
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

// }

// @lc code=end

/*
 // @lcpr case=start
 // [1,2,4]\n[1,3,4]\n
 // @lcpr case=end

 // @lcpr case=start
 // []\n[]\n
 // @lcpr case=end

 // @lcpr case=start
 // []\n[0]\n
 // @lcpr case=end

  */
