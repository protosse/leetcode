#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
# https://leetcode.cn/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (48.71%)
# Likes:    570
# Dislikes: 0
# Total Accepted:    80.3K
# Total Submissions: 164.8K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 0
# 输出：0
# 
# 
# 
# 提示: 
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # 排除下特殊情况
        if k <= 1:
            return 0
        left, right = 0, 0
        res = 1
        count = 0
        while right < len(nums):
            c = nums[right]
            res = c * res

            while res >= k:
                d = nums[left]
                left += 1
                res = res / d
            # res的值是 left 到 right 的值的积，因此每次移动 right 后，符合条件的子数组应该是
            # [nums[right]]
            # [nums[right], nums[right - 1]] 
            # 一直到 [nums[right], nums[right - 1] ... , nums[left]]
            count += right - left + 1
            # 因为要算 count 就把 right 加1的操作放到后面啦
            right += 1

        return count

# @lc code=end

