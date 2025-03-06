之前[21 题](21.合并两个有序链表)已经做过了如何合并两个有序链表，这里变成了 K 个升序链表，一个解法是用分治的思想，把这 K 个链表两两合并

```python
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None

    def merge(lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        l1 = merge(lists, left, mid)
        l2 = merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)

    return merge(lists, 0, len(lists) - 1)
```

还有一个做法是使用[优先级队列](0.Base/7.二叉堆.ipynb)，把链表节点放入一个最小堆，就可以每次获得 k 个节点中的最小节点，放入结果链表中
