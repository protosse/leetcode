#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#
# https://leetcode.cn/problems/matrix-block-sum/description/
#
# algorithms
# Medium (75.56%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    18.9K
# Total Submissions: 25.1K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素
# mat[r][c] 的和： 
# 
# 
# i - k 
# j - k  且
# (r, c) 在矩阵内。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# 示例 2：
# 
# 
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# 
# 提示：
# 
# 
# m == mat.length
# n == mat[i].length
# 1 
# 1 
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        pass
# @lc code=end

