#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (48.86%)
# Likes:    1127
# Dislikes: 0
# Total Accepted:    275.8K
# Total Submissions: 564.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

from typing import List

# @lc code=start


class Solution:
    def spiralOrder_iter(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        upper_bound = 0
        lower_bound = m - 1
        left_bound = 0
        right_bound = n - 1

        res = []

        while len(res) < m * n:
            if upper_bound <= lower_bound:
                # 从顶部由左向右遍历
                for j in range(left_bound, right_bound + 1):
                    res.append(matrix[upper_bound][j])
                # 上边界下移
                upper_bound += 1
            if left_bound <= right_bound:
                # 从右侧由上到下遍历
                for i in range(upper_bound, lower_bound + 1):
                    res.append(matrix[i][right_bound])
                # 右边界左移
                right_bound -= 1
            if upper_bound <= lower_bound:
                # 从底部由右向左遍历
                for j in range(right_bound, left_bound-1, -1):
                    res.append(matrix[lower_bound][j])
                # 下边界上移
                lower_bound -= 1
            if left_bound <= right_bound:
                # 从左侧由下往上遍历
                for i in range(lower_bound, upper_bound - 1, -1):
                    res.append(matrix[i][left_bound])
                # 左边界右移
                left_bound += 1
        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
            
# @lc code=end

