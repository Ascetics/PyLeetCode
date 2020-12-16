from functools import reduce

nums = [-1, 0, 1, 2, -1, -4]


# nums = [0, 0, 0, 0]


class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        dic = {}
        res = []
        for n in nums:
            v = dic.get(n)
            if v:
                dic[n] = v + 1
            else:
                dic[n] = 1

        print(nums)
        for i, x in enumerate(nums):
            dic[x] = dic[x] - 1
            for j, y in enumerate(nums[i + 1:]):
                dic[y] = dic[y] - 1
                z = 0 - x - y
                if z >= y:
                    remain = dic.get(z)
                    if remain and remain > 0:
                        r = [x, y, z]
                        if r not in res:
                            res.append(r)
                dic[y] = dic[y] + 1
            dic[x] = dic[x] + 1

        return res


s = Solution()
print(s.threeSum(nums))
