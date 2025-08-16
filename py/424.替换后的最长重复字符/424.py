#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30104
#
# [424] 替换后的最长重复字符
#
# https://leetcode.cn/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (55.55%)
# Likes:    914
# Dislikes: 0
# Total Accepted:    108.8K
# Total Submissions: 195.4K
# Testcase Example:  '"ABAB"\n2'
#
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
#
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
#
#
#
# 示例 1：
#
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#
#
# 示例 2：
#
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^5
# s 仅由大写英文字母组成
# 0 <= k <= s.length
#
#
#


# @lc code=start

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """可以把这道题理解为
        求字符串中一个最长的区间，该区间内的出现次数较少的字符的总个数不超过 k
        """
        left = 0
        res = 0
        counter = Counter()
        for right in range(len(s)):
            c = s[right]
            counter[c] += 1
            # right - left + 1 是这个左闭右闭区间的总长度
            # counter.most_common(1)[0][1] 是区间中出现次数最多的字符的数量
            # 相减就是区间中其它出现次数较少的字符的总个数
            while right - left + 1 - counter.most_common(1)[0][1] > k:
                d = s[left]
                counter[d] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# @lc code=end


#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#
