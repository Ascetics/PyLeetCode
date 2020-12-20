# 14. 最长公共前缀
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#拍排
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-common-prefix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        """
        按照字母序排大小，最小字符串和最大字符串的公共前缀就是结论。可反证。
        :param strs: List[str]
        :return: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        smin, smax = min(strs), max(strs)
        length = min(len(smin), len(smax))
        comm = ''
        for i in range(length):
            if smin[i] == smax[i]:
                comm += smin[i]
            else:
                return comm
        return comm

s1 = ["flower", "flow", "flight"]
s2 = ["dog", "racecar", "car"]
s3 = []
s4 = ['']
s5 = ['', '']
s6 = ['a']
sol = Solution()
print(s1, sol.longestCommonPrefix(s1))
print(s2, sol.longestCommonPrefix(s2))
print(s3, sol.longestCommonPrefix(s3))
print(s4, sol.longestCommonPrefix(s4))
print(s5, sol.longestCommonPrefix(s5))
print(s6, sol.longestCommonPrefix(s6))
