#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (44.88%)
# Likes:    2819
# Dislikes: 0
# Total Accepted:    977.7K
# Total Submissions: 2.2M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向后跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
#
#
# 0 <= j <= nums[i]
# i + j < n
#
#
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 示例 2:
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]
#
#
#

# @lc code=start

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step = 0
        cur_i = 0  # 当前能够到达的最远索引
        next_i = 0  # 下一步能到达的最远索引
        for i, j in enumerate(nums):
            next_i = max(next_i, i + j)
            if i == cur_i:
                step += 1
                cur_i = next_i
                # 如果能到达终点，就可以结束了
                if next_i >= len(nums) - 1:
                    break
        return step


# @lc code=end


#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#
