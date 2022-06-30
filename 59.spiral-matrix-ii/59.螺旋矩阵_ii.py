#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (76.19%)
# Likes:    747
# Dislikes: 0
# Total Accepted:    210.8K
# Total Submissions: 276.9K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        upper_bound = 0
        lower_bound = n - 1
        left_bound = 0
        right_bound = n - 1

        num = 1
        while num <= n * n:
            if upper_bound <= lower_bound:
                # 从顶部由左向右遍历
                for j in range(left_bound, right_bound + 1):
                    matrix[upper_bound][j] = num
                    num += 1
                # 上边界下移
                upper_bound += 1
            if left_bound <= right_bound:
                # 从右侧由上到下遍历
                for i in range(upper_bound, lower_bound + 1):
                    matrix[i][right_bound] = num
                    num += 1
                # 右边界左移
                right_bound -= 1
            if upper_bound <= lower_bound:
                # 从底部由右向左遍历
                for j in range(right_bound, left_bound-1, -1):
                    matrix[lower_bound][j] = num
                    num += 1
                # 下边界上移
                lower_bound -= 1
            if left_bound <= right_bound:
                # 从左侧由下往上遍历
                for i in range(lower_bound, upper_bound - 1, -1):
                    matrix[i][left_bound] = num
                    num += 1
                # 左边界右移
                left_bound += 1
        return matrix

# @lc code=end

