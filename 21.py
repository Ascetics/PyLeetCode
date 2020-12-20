# 21. 合并两个有序链表
# 将两个升序链表合并为一个新的
# 升序
# 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
# 来源：力扣（LeetCode）
# 链接：https: // leetcode - cn.com / problems / merge - two - sorted - lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        注意l1、l2为空的情况
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """
        cur = dum = ListNode()
        while l1 or l2:
            if l1 and not l2:
                cur.next = l1
                break
            elif l2 and not l1:
                cur.next = l2
                break
            else:
                if l1.val <= l2.val:
                    cur.next, l1 = l1, l1.next
                else:
                    cur.next, l2 = l2, l2.next
                cur = cur.next
        return dum.next


def show(head):
    while head:
        print(head.val, end='')
        head = head.next
        print('->' if head else '\n', end='')


h11 = ListNode(1)
h12 = h11.next = ListNode(2)
h13 = h12.next = ListNode(4)

h21 = ListNode(1)
h22 = h21.next = ListNode(3)
h23 = h22.next = ListNode(4)

show(h11)
show(h21)
s = Solution()
res = s.mergeTwoLists(h11, h21)
show(res)
