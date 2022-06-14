最简单的做法是
``` Python
class NumArray:

    def __init__(self, nums: List[int]):
      self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
      return sum(self.nums[left:right+1])

```
不过最优的解法是使用前缀和，核心思路是我们 new 一个新的数组 preSum 出来，preSum[i] 记录 nums[0..i-1] 的累加和![](https://labuladong.github.io/algo/images/差分数组/1.jpeg)
如果我想求索引区间 [1, 4] 内的所有元素之和，就可以通过 preSum[5] - preSum[1] 得出。这样，sumRange 函数仅仅需要做一次减法运算，避免了每次进行 for 循环调用，最坏时间复杂度为常数 O(1)