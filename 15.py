"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？
请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。
示例：

给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 0, 0]


class Solution:
    def threeSum(self, nums):
        """
        0、nums至少有3个元素
        1、排序
        2、a<b<c a必须<=0，如果a>0那就结束
        3、避免重复，a,b,c都要避免重复
        :param nums:
        :return:
        """
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        res = []
        for i, a in enumerate(nums):
            if a > 0:
                return res
            else:
                if i > 0 and a == nums[i - 1]:
                    continue  # 避免a重复
                left, right = i + 1, len(nums) - 1
                while left < right:
                    if a + nums[left] + nums[right] < 0:
                        left += 1
                    elif a + nums[left] + nums[right] > 0:
                        right -= 1
                    else:
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1  # 避免b重复
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1  # 避免c重复
                        res.append([a, nums[left], nums[right]])
                        left, right = left + 1, right - 1
        return res


s = Solution()
print(s.threeSum(nums1))
print(s.threeSum(nums2))
