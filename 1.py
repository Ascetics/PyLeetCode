class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，
    并返回他们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

    示例:

    给定 nums = [2, 7, 11, 15], target = 9

    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

    来源：力扣（LeetCode）
    链接：https://leetcode-cn.com/problems/two-sum
    著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
    """

    def twoSum(self, nums, target):
        """
        用dict模拟hashmap方法，改进
        :param nums:
        :param target:
        :return:
        """
        dic = {}
        for index, n in enumerate(nums):
            dic[n] = index
            pass
        # 由于上面使用了dic，数值相同，那么dic只会记录下标最大的那个
        # 所以，遍历的时候，只能从nums遍历，不能从dic遍历，否则会漏掉类似6=3+3的情况
        for index_i, i in enumerate(nums):
            j = target - i
            index_j = dic.get(j)
            if index_j is not None and index_j != index_i:
                return [index_i, index_j]

    pass


if __name__ == '__main__':
    solution = Solution()
    '''
    三组测试用例
    '''
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))
    nums = [3, 2, 6]
    target = 6
    print(solution.twoSum(nums, target))
    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))
    pass
