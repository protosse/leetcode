/*
 * @lc app=leetcode.cn id=896 lang=golang
 *
 * [896] 单调数列
 *
 * https://leetcode-cn.com/problems/monotonic-array/description/
 *
 * algorithms
 * Easy (58.73%)
 * Likes:    132
 * Dislikes: 0
 * Total Accepted:    55.6K
 * Total Submissions: 94.6K
 * Testcase Example:  '[1,2,2,3]'
 *
 * 如果数组是单调递增或单调递减的，那么它是单调的。
 *
 * 如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A
 * 是单调递减的。
 *
 * 当给定的数组 A 是单调数组时返回 true，否则返回 false。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 * 输入：[1,2,2,3]
 * 输出：true
 *
 *
 * 示例 2：
 *
 * 输入：[6,5,4,4]
 * 输出：true
 *
 *
 * 示例 3：
 *
 * 输入：[1,3,2]
 * 输出：false
 *
 *
 * 示例 4：
 *
 * 输入：[1,2,4,5]
 * 输出：true
 *
 *
 * 示例 5：
 *
 * 输入：[1,1,1]
 * 输出：true
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= A.length <= 50000
 * -100000 <= A[i] <= 100000
 *
 *
 */

package main

import (
	"fmt"
)

// @lc code=start
func isMonotonic(A []int) bool {
	increase := 0
	var last int
	for i := 0; i < len(A); i++ {
		if i != 0 {
			var re int
			if A[i] != last && increase == 0 {
				if A[i] > last {
					increase = 1
				} else {
					increase = -1
				}
			}

			if A[i] == last {
				re = 0
			} else if A[i] > last {
				re = 1
			} else {
				re = -1
			}

			if re != 0 && increase != re {
				return false
			}
		}
		last = A[i]
	}
	return true
}

// @lc code=end

func main() {
	fmt.Println(isMonotonic([]int{11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5}))
}
