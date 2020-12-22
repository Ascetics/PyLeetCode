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
        """
        特判，如果root为空，那么返回[]
        root进入队列q，下一层队列q_sub和结果r都为[]，方向最初是向右
        反向遍历q,相当于队列出队，进入r。
        判断方向向右，先加左再加右。得到本层结果r和下一层队列的反向q_sub
        更新队列q和方向进入下一层。
        上一层得到的是反向的队列，反向遍历顺序还是对的。（第一层因为只有1个node，所以正反一样）
        判断方向向左，先加右再加左。
        周而复始，直到队列q为空。        
        """
        if not root: return []
        q, right, res = [root], True, []
        while len(q) > 0:
            q_sub, r = [], []
            for n in reversed(q):
                r.append(n.val)
                if right:
                    if n.left: q_sub.append(n.left)
                    if n.right: q_sub.append(n.right)
                else:
                    if n.right: q_sub.append(n.right)
                    if n.left: q_sub.append(n.left)
            if len(r) > 0: res.append(r)
            q, right = q_sub, not right
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
    
