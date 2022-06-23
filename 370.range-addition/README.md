差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行增减，比如说，我给你输入一个数组 nums，然后又要求给区间 nums[2..6] 全部加 1，再给 nums[3..9] 全部减 3，再给 nums[0..4] 全部加 2

类似[前缀和](../303.range-sum-query-immutable/)技巧构造的 prefix 数组，我们先对 nums 数组构造一个 diff 差分数组，diff[i] 就是 nums[i] 和 nums[i-1] 之差

``` python
nums = [8, 2, 6, 3, 1]
diff = [0 for _ in range(len(nums))] # [8, -6, 4, -3, -2]
diff[0] = nums[0]
for i in range(1, len(nums)):
    diff[i] = nums[i] - nums[i - 1]
```

通过这个 diff 差分数组是可以反推出原始数组 nums 的，代码如下

``` python
res = [0 for _ in range(len(diff))]
res[0] = diff[0]
for i in range(1, len(diff)):
    res[i] = res[i - 1] + diff[i]
```

如果你想对区间 nums[i..j] 的元素全部加 3，那么只需要让 diff[i] += 3，然后再让 diff[j+1] -= 3 即可

原理很简单，回想 diff 数组反推 nums 数组的过程，diff[i] += 3 意味着给 nums[i..] 所有的元素都加了 3，然后 diff[j+1] -= 3 又意味着对于 nums[j+1..] 所有元素再减 3，那综合起来，是不是就是对 nums[i..j] 中的所有元素都加 3 了？