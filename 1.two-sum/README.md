基本的方法是两个循环遍历，找出加起来等于 target 的两个数。

时间复杂度小于 O(n^2)的方法，可以用一个字典 key 与 value 都为 int 的 dict 来记录。每次遍历数组时，将要求的数字，也就是 target - nums[index]作为 key，index 作为 value 存入字典，在更新字典前也要检查字典中是否存在 target - nums[index] 的 key，如果存在，则说明找到了，输出 dict[key]和当前的 index 就是需要的结果。
