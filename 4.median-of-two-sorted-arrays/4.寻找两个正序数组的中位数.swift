/*
 * @lc app=leetcode.cn id=4 lang=swift
 *
 * [4] 寻找两个正序数组的中位数
 *
 * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (41.06%)
 * Likes:    4826
 * Dislikes: 0
 * Total Accepted:    576.3K
 * Total Submissions: 1.4M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
 *
 * 算法的时间复杂度应该为 O(log (m+n)) 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums1 = [1,3], nums2 = [2]
 * 输出：2.00000
 * 解释：合并数组 = [1,2,3] ，中位数 2
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums1 = [1,2], nums2 = [3,4]
 * 输出：2.50000
 * 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums1 = [0,0], nums2 = [0,0]
 * 输出：0.00000
 *
 *
 * 示例 4：
 *
 *
 * 输入：nums1 = [], nums2 = [1]
 * 输出：1.00000
 *
 *
 * 示例 5：
 *
 *
 * 输入：nums1 = [2], nums2 = []
 * 输出：2.00000
 *
 *
 *
 *
 * 提示：
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */

// @lc code=start
class Solution {
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        let count = nums1.count + nums2.count
        var i = 0, j = 0
        var value = 0
        var pre = 0
        for _ in 0 ... count / 2 {
            pre = value
            if let n1 = nums1[safe: i], let n2 = nums2[safe: j] {
                if n1 < n2 {
                    value = n1
                    i += 1
                } else {
                    value = n2
                    j += 1
                }
            } else if let n1 = nums1[safe: i] {
                value = n1
                i += 1
            } else if let n2 = nums2[safe: j] {
                value = n2
                j += 1
            }
        }

        if count % 2 != 0 {
            return Double(value)
        } else {
            return Double(value + pre) / 2
        }
    }
}

extension Collection {
    subscript(safe index: Index) -> Element? {
        return indices.contains(index) ? self[index] : nil
    }
}

// @lc code=end
