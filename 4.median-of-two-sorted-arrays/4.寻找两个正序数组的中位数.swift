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
    /// 第k小
    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        let m = nums1.count
        let n = nums2.count
        if (m + n) % 2 == 1 {
            return Double(getKth(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 1) / 2))
        } else {
            return Double(getKth(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 1) / 2) + getKth(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 2) / 2)) * 0.5
        }
    }

    func getKth(_ nums1: [Int], _ start1: Int, _ end1: Int, _ nums2: [Int], _ start2: Int, _ end2: Int, _ k: Int) -> Int {
        let len1 = end1 - start1 + 1
        let len2 = end2 - start2 + 1
        // 保证nums1是短的那个数组
        if len1 > len2 {
            return getKth(nums2, start2, end2, nums1, start1, end1, k)
        }

        if len1 == 0 {
            return nums2[start2 + k - 1]
        }

        if k == 1 {
            return min(nums1[start1], nums2[start2])
        }

        let i = start1 + min(len1, k / 2) - 1
        let j = start2 + min(len2, k / 2) - 1

        if nums1[i] > nums2[j] {
            return getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        } else {
            return getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
        }
    }

    /// 分割线
    func findMedianSortedArrays_separate(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var nums1 = nums1
        var nums2 = nums2
        // 保证nums1是短的那个数组
        if nums1.count > nums2.count {
            let temp = nums1
            nums1 = nums2
            nums2 = temp
        }

        let m = nums1.count
        let n = nums2.count

        // 分割线左边的元素个数
        let totalLeft = (m + n + 1) / 2

        // 在 nums1 的区间 [0, m] 里查找恰当的分割线，
        // 使得 nums1[i - 1] <= nums2[j] && nums2[j - 1] <= nums1[i]
        var left = 0
        var right = m

        while left < right {
            let i = left + (right - left + 1) / 2
            let j = totalLeft - i
            if nums1[i - 1] > nums2[j] {
                // 下一轮搜索的区间 [left, i - 1]
                right = i - 1
            } else {
                // 下一轮搜索的区间 [i, right]
                left = i
            }
        }

        let i = left
        let j = totalLeft - i

        let nums1LeftMax = i == 0 ? Int.min : nums1[i - 1]
        let nums1RightMin = i == m ? Int.max : nums1[i]
        let nums2LeftMax = j == 0 ? Int.min : nums2[j - 1]
        let nums2RightMin = j == n ? Int.max : nums2[j]

        if (m + n) % 2 == 1 {
            return Double(max(nums1LeftMax, nums2LeftMax))
        } else {
            return Double(max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2
        }
    }

    /// 归并
    func findMedianSortedArrays_loop(_ nums1: [Int], _ nums2: [Int]) -> Double {
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
