# 28. 实现 strStr()
# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，
# 在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。
#
# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
# 说明:
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。
# 这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-strstr
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif not haystack:
            return -1
        else:
            return haystack.find(needle)


if __name__ == '__main__':
    sol = Solution()

    haystack1, needle1 = "hello", "ll"
    haystack2, needle2 = "aaaaa", "bba"
    haystack3, needle3 = 'hello', ''
    haystack4, needle4 = '', ''
    haystack5, needle5 = '', 'bba'
    print(sol.strStr(haystack1, needle1))
    print(sol.strStr(haystack2, needle2))
    print(sol.strStr(haystack3, needle3))
    print(sol.strStr(haystack4, needle4))
    print(sol.strStr(haystack5, needle5))
