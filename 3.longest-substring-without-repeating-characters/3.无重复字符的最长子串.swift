/*
 * @lc app=leetcode.cn id=3 lang=swift
 *
 * [3] 无重复字符的最长子串
 *
 * https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (38.31%)
 * Likes:    6639
 * Dislikes: 0
 * Total Accepted:    1.4M
 * Total Submissions: 3.6M
 * Testcase Example:  '"abcabcbb"'
 *
 * 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: s = "abcabcbb"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
 *
 *
 * 示例 2:
 *
 *
 * 输入: s = "bbbbb"
 * 输出: 1
 * 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
 *
 *
 * 示例 3:
 *
 *
 * 输入: s = "pwwkew"
 * 输出: 3
 * 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
 * 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 *
 *
 * 示例 4:
 *
 *
 * 输入: s = ""
 * 输出: 0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0
 * s 由英文字母、数字、符号和空格组成
 *
 *
 */

// @lc code=start
class Solution {
    func lengthOfLongestSubstring(_ s: String) -> Int {
        var start = 0
        var maxLength = 0
        var dict = [String.Element: Int]()
        for (i, v) in s.enumerated() {
            if let index = dict[v], index >= start {
                start = index + 1
            }
            maxLength = max(maxLength, i - start + 1)
            dict[v] = i
        }
        return maxLength
    }

    func lengthOfLongestSubstring_array(_ s: String) -> Int {
        var maxLength = 0
        var dis = [String.Element]()
        for v in s {
            if let index = dis.firstIndex(of: v) {
                dis.removeSubrange(0 ... index)
            }
            dis.append(v)
            maxLength = max(dis.count, maxLength)
        }
        return maxLength
    }
}

// @lc code=end
