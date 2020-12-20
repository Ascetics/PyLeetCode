# 20. 有效的括号
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
#     左括号必须用相同类型的右括号闭合。
#     左括号必须以正确的顺序闭合。
#
# 注意空字符串可被认为是有效字符串。
#
# 示例 1:
# 输入: "()"
# 输出: true
#
# 示例 2:
# 输入: "()[]{}"
# 输出: true
#
# 示例 3:
# 输入: "(]"
# 输出: false
#
# 示例 4:
# 输入: "([)]"
# 输出: false
#
# 示例 5:
# 输入: "{[]}"
# 输出: true
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def isValid(self, s: str) -> bool:
        """
        用stack解决
        :param s: str
        :return: bool
        """
        if len(s) == 0:
            return True
        buf = []
        while s:
            x, s = s[0], s[1:]
            if x == '(' or x == '[' or x == '{':
                buf += x
            else:
                if len(buf) == 0:
                    return False
                buf, y = buf[:-1], buf[-1]
                if y is None or (y != '(' and x == ')') or (y != '[' and x == ']') \
                        or (y != '{' and x == '}'):
                    return False
        return len(buf) == 0


if __name__ == '__main__':
    sol = Solution()

    s0 = ''
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = ']'

    print(s0, sol.isValid(s0))
    print(s1, sol.isValid(s1))
    print(s2, sol.isValid(s2))
    print(s3, sol.isValid(s3))
    print(s4, sol.isValid(s4))
    print(s5, sol.isValid(s5))
    print(s6, sol.isValid(s6))
