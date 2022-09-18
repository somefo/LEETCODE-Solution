# Code Solution for leetcode 25. Reverse Nodes in k-Group
# 1<= k <= n
# 1<= n <= 5000
# n is the length of the linked list

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def findnode(node, i):
            while i > 0:
                if node is None:
                    break
                node = node.next
                i -= 1
            return node

        prev = None
        i, j = 0, k - 1
        first, last = findnode(head, i), findnode(head, j)
        while last is not None:
            node = first.next
            if i == j:
                if prev is None:
                    head = first
                    prev = findnode(first, k - 1)
                    first = prev.next
                    last = findnode(first, k - 1)
                    i += k
                    j = i + k - 1
                else:
                    prev.next = first
                    prev = findnode(first, k - 1)
                    first = prev.next
                    last = findnode(first, k - 1)
                    i += k
                    j = i + k - 1
            else:
                first.next = last.next
                last.next = first
                i += 1
                first = node
        return head


def build_linkedlist(nums):
    head = ListNode(nums[0])
    node = head
    for i in range(1, len(nums)):
        node.next = ListNode(nums[i])
        node = node.next
    return head


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = build_linkedlist(nums)
    k = 3
    solution = Solution()
    head = solution.reverseKGroup(head, k)
    while head is not None:
        print(head.val, end= ' ')
        head = head.next