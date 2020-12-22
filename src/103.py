'''
103. 二叉树的锯齿形层序遍历

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

    3
   / \
  9  20
    /  \
   15   7

返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root: TreeNode):
        if not root: return []
        q, right, res = [root], True, []
        while len(q) > 0:
            q_sub, r = [], []
            for i in range(len(q) - 1, -1, -1):
                r.append(q[i].val)
                if right:
                    if q[i].left: q_sub.append(q[i].left)
                    if q[i].right: q_sub.append(q[i].right)
                else:
                    if q[i].right: q_sub.append(q[i].right)
                    if q[i].left: q_sub.append(q[i].left)
            if len(r) > 0:res.append(r)
            q = q_sub
            right = not right
        return res
        
        
if __name__ == '__main__':
    root0 = None
    
    left, right = TreeNode(15), TreeNode(7)
    root = TreeNode(20)
    root.left, root.right = left, right
    left, right = TreeNode(9), root
    root = TreeNode(3)
    root.left, root.right = left, right
    root1 = root
    
    root2 = TreeNode(17)
    
    sol = Solution()
    print(sol.zigzagLevelOrder(root0))
    print(sol.zigzagLevelOrder(root1))
    print(sol.zigzagLevelOrder(root2))
    
