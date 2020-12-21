# 35. 搜索插入位置
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
#
# 示例 2:
# 输入: [1,3,5,6], 2
# 输出: 1
#
# 示例 3:
# 输入: [1,3,5,6], 7
# 输出: 4
#
# 示例 4:
# 输入: [1,3,5,6], 0
# 输出: 0
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-insert-position
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        """
        二分法查找，最终left==right，判断nums[left]和target大小返回left或left+1
        :param nums:
        :param target:
        :return:
        """
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return left if target <= nums[left] else left + 1


if __name__ == '__main__':
    sol = Solution()

    nums0, target0 = [], 0
    nums1, target1 = [1, 3, 5, 6], 5
    nums2, target2 = [1, 3, 5, 6], 2
    nums3, target3 = [1, 3, 5, 6], 7
    nums4, target4 = [1, 3, 5, 6], 0

    print(sol.searchInsert(nums0, target0), nums0, target0)
    print(sol.searchInsert(nums1, target1), nums1, target1)
    print(sol.searchInsert(nums2, target2), nums2, target2)
    print(sol.searchInsert(nums3, target3), nums3, target3)
    print(sol.searchInsert(nums4, target4), nums4, target4)

