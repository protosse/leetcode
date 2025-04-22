![](image/26.excalidraw.png)
可以使用快慢指针

让慢指针 slow 走在后面，快指针 fast 走在前面探路，找到一个不重复的元素就让 slow 前进一步并赋值。

这样，就保证了 nums[0..slow] 都是无重复的元素，当 fast 指针遍历完整个数组 nums 后，nums[0..slow] 就是整个数组去重之后的结果。
