#
# @lc app=leetcode.cn id=187 lang=python3
# @lcpr version=30104
#
# [187] 重复的DNA序列
#
# https://leetcode.cn/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (55.25%)
# Likes:    615
# Dislikes: 0
# Total Accepted:    187.2K
# Total Submissions: 338.4K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# DNA序列 由一系列核苷酸组成，缩写为 'A', 'C', 'G' 和 'T'.。
#
#
# 例如，"ACGAATTCCG" 是一个 DNA序列 。
#
#
# 在研究 DNA 时，识别 DNA 中的重复序列非常有用。
#
# 给定一个表示 DNA序列 的字符串 s ，返回所有在 DNA 分子中出现不止一次的 长度为 10 的序列(子字符串)。你可以按 任意顺序
# 返回答案。
#
#
#
# 示例 1：
#
# 输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 输出：["AAAAACCCCC","CCCCCAAAAA"]
#
#
# 示例 2：
#
# 输入：s = "AAAAAAAAAAAAA"
# 输出：["AAAAAAAAAA"]
#
#
#
#
# 提示：
#
#
# 0 <= s.length <= 10^5
# s[i]=='A'、'C'、'G' or 'T'
#
#
#

from typing import List


# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        left, right = 0, 10
        window = {}
        res = []
        while right <= len(s):
            c = s[left:right]
            left += 1
            right += 1
            window[c] = window.get(c, 0) + 1
            if window[c] > 1 and c not in res:
                res.append(c)

        return res


# @lc code=end


#
# @lcpr case=start
# "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"\n
# @lcpr case=end

# @lcpr case=start
# "AAAAAAAAAAAAA"\n
# @lcpr case=end

#
