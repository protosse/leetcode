#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (48.92%)
# Likes:    253
# Dislikes: 0
# Total Accepted:    39.1K
# Total Submissions: 79.8K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
# 
# 如果不存在满足条件的子数组，则返回 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2 
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4. 
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4. 
# 因此，满足题意的最长子数组的长度为 2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4 
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
# 
# 
# 示例 3：
# 
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#

from collections import deque
from typing import List

# @lc code=start
class Solution:
    # 超时版本
    def longestSubarray_timeout(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        count = 0
        while right < len(nums):
            c = nums[right]

            for i in range(left, right):
                res = abs(c - nums[i])
                if res > limit:
                    left = i + 1
            count = max(count, right - left + 1)
            right += 1
        return count

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left, right = 0, 0
        count = 0

        # maxQue为一个单调递减的序列
        # minQue为一个单调递增的序列
        maxQue, minQue = deque(), deque()

        while right < len(nums):
            c = nums[right]

            # maxQue中记录比c大的值
            while maxQue and maxQue[-1] < c:
                maxQue.pop()

            # minQue中记录比c小的值
            while minQue and minQue[-1] > c:
                minQue.pop()

            maxQue.append(c)
            minQue.append(c)

            while maxQue and minQue and maxQue[0] - minQue[0] > limit:
                if nums[left] == minQue[0]:
                    minQue.popleft()
                if nums[left] == maxQue[0]:
                    maxQue.popleft()
                left += 1

            count = max(count, right - left + 1)
            right += 1
        return count

# @lc code=end


nums = [24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39]
print(Solution().longestSubarray(nums, 87))