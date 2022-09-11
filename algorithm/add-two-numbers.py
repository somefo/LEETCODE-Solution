# Code solution for leetcode

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first = ListNode(0)
        head = first
        add = 0
        while l1 or l2:
            a, b = 0, 0
            if l1:
                a = l1.val
                l1 = l1.next
            if l2:
                b = l2.val
                l2 = l2.next
            c = a + b + add
            if c < 10:
                node = ListNode(c)
                head.next = node
                head = node
                add = 0
            else:
                d = c % 10
                node = ListNode(d)
                head.next = node
                head = node
                add = 1

        if add == 1:
            node = ListNode(1)
            head.next = node

        return first.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    s = Solution()
    res = s.addTwoNumbers(l1, l2)
    while res:
        print(res.val, end=' ')
        res = res.next