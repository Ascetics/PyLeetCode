# 给出两个 非空 的链表用来表示两个非负的整数。
# 其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def toInt(head: ListNode) -> int:
    return 0 if not head else head.val + 10 * toInt(head.next)


def printInt(func):
    def wrapper(*args, **kwargs):
        print(toInt(args[1]))
        print(toInt(args[2]))
        res = func(*args, **kwargs)
        print(toInt(res))
        return res

    return wrapper


class Solution:

    @printInt
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        注意进位cap
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        cur = dum = ListNode()
        cap = 0
        while l1 or l2 or cap > 0:
            if l1 and l2:
                cap, s = divmod(l1.val + l2.val + cap, 10)
                cur.next, l1, l2 = ListNode(s), l1.next, l2.next
            elif l1 and not l2:
                cap, s = divmod(l1.val + cap, 10)
                cur.next, l1 = ListNode(s), l1.next
            elif l2 and not l1:
                cap, s = divmod(l2.val + cap, 10)
                cur.next, l2 = ListNode(s), l2.next
            else:
                cap, s = divmod(cap, 10)
                cur.next = ListNode(s)
            cur = cur.next
        return dum.next


sol = Solution()

h01 = ListNode(0)

h11 = ListNode(2)
h12 = h11.next = ListNode(4)
h13 = h12.next = ListNode(3)

h21 = ListNode(5)
h22 = h21.next = ListNode(6)
h23 = h22.next = ListNode(4)

h31 = ListNode(9)
h32 = h31.next = ListNode(9)
h33 = h32.next = ListNode(9)
h34 = h33.next = ListNode(9)
h35 = h34.next = ListNode(9)
h36 = h35.next = ListNode(9)
h37 = h36.next = ListNode(9)

h41 = ListNode(9)
h42 = h41.next = ListNode(9)
h43 = h42.next = ListNode(9)
h44 = h43.next = ListNode(9)

sol.addTwoNumbers(h31, h41)
