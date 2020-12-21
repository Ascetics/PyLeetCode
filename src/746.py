# 746. 使用最小花费爬楼梯
# 
# 数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
# 每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
# 您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。
# 
# 示例 1:
# 输入: cost = [10, 15, 20]
# 输出: 15
# 解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
# 
# 示例 2:
# 输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出: 6
# 解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
# 
# 注意：
# cost 的长度将会在 [2, 1000]。
# 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
# 
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:

    def minCostClimbingStairs(self, cost) -> int:
        """
        cost[i]连接cost[i+1]和cost[i+2]，边的长度为cost[i]
        这样连起来的图，选择最短路径
        从cost[0]出发走一次，从cost[1]出发走一次，取两者较小的
        """
        # 从cost[0]出发走一次
        cost0 = cost
        acc0 = [0] * (1 + len(cost0))
        init0 = [True] * (1 + len(cost0))
        for i, _ in enumerate(cost0):
            if i + 1 <= len(cost0) and (init0[i + 1] or acc0[i] + cost0[i] < acc0[i + 1]):
                acc0[i + 1], init0[i + 1] = acc0[i] + cost0[i], False                 
            if i + 2 <= len(cost0) and (init0[i + 2] or acc0[i] + cost0[i] < acc0[i + 2]):
                acc0[i + 2], init0[i + 2] = acc0[i] + cost0[i], False
           
        # 从cost[1]出发走一次
        cost1 = cost[1:]
        acc1 = [0] * (1 + len(cost1))
        init1 = [True] * (1 + len(cost1))
        for i, _ in enumerate(cost1):
            if i + 1 <= len(cost1) and (init1[i + 1] or acc1[i] + cost1[i] < acc1[i + 1]):
                acc1[i + 1], init1[i + 1] = acc1[i] + cost1[i], False
            if i + 2 <= len(cost1) and (init1[i + 2] or acc1[i] + cost1[i] < acc1[i + 2]):
                acc1[i + 2], init1[i + 2] = acc1[i] + cost1[i], False
        
        return acc0[-1] if acc0[-1] < acc1[-1] else acc1[-1]

    
if __name__ == '__main__':
    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    cost3 = [0, 0, 0, 0]
    
    sol = Solution()
    print(cost1, sol.minCostClimbingStairs(cost1), sep='\n')
    print(cost2, sol.minCostClimbingStairs(cost2), sep='\n')
    print(cost3, sol.minCostClimbingStairs(cost3), sep='\n')
    
