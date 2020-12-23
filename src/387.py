# 387. 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 
# 示例：
# s = "leetcode"
# 返回 0
# 
# s = "loveleetcode"
# 返回 2
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:

    def firstUniqChar(self, s: str) -> int:
        """
        空字符串直接返回-1
        遍历一遍，统计个数，放入字典
        再遍历一遍，遇到个数为1的返回位置
        否则则返回-1
        """
        if len(s) == 0: return -1
        
        dic = {}
        for c in s:
            dic[c] = dic.setdefault(c, 0) + 1
        for i, c in enumerate(s):
            if dic[c] == 1: return i
        return -1
    
    
if __name__ == '__main__':
    s0 = ""
    s1 = "leetcode"
    s2 = "loveleetcode"
    
    sol = Solution()
    print(sol.firstUniqChar(s0))
    print(sol.firstUniqChar(s1))
    print(sol.firstUniqChar(s2))
    
    pass
