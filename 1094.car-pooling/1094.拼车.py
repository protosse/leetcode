#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
# https://leetcode.cn/problems/car-pooling/description/
#
# algorithms
# Medium (54.40%)
# Likes:    187
# Dislikes: 0
# Total Accepted:    49.4K
# Total Submissions: 90.7K
# Testcase Example:  '[[2,1,5],[3,3,7]]\n4'
#
# 车上最初有 capacity 个空座位。车 只能 向一个方向行驶（也就是说，不允许掉头或改变方向）
# 
# 给定整数 capacity 和一个数组 trips ,  trip[i] = [numPassengersi, fromi, toi] 表示第 i
# 次旅行有 numPassengersi 乘客，接他们和放他们的位置分别是 fromi 和 toi 。这些位置是从汽车的初始位置向东的公里数。
# 
# 当且仅当你可以在所有给定的行程中接送所有乘客时，返回 true，否则请返回 false。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 4
# 输出：false
# 
# 
# 示例 2：
# 
# 
# 输入：trips = [[2,1,5],[3,3,7]], capacity = 5
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= trips.length <= 1000
# trips[i].length == 3
# 1 <= numPassengersi <= 100
# 0 <= fromi < toi <= 1000
# 1 <= capacity <= 10^5
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = 1001
        nums = [0 for _ in range(length)]
        diff = [0 for _ in range(length)]
        for v, i, j in trips:
            diff[i] += v
            diff[j] -= v

        nums[0] = diff[0]
        if nums[0] > capacity:
            return False

        for i in range(1, length):
            nums[i] = nums[i - 1] + diff[i]
            if nums[i] > capacity:
                return False
        return True
        

# @lc code=end

