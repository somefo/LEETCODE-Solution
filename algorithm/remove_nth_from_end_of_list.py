# Description: Given the head of a linked list, remove the nth node 
# from the end of the list and return its head.
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Input: head = [1], n = 1
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer1 = ListNode() # virtual node
        pointer1.next = head
        pointer2 = pointer1 # use two pointer to do one pass
        while n > 0:
            n -= 1
            pointer2 = pointer2.next
        # one pass
        while pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        # in case head is removed
        if head == pointer1.next:
            head = head.next
        pointer1.next = pointer1.next.next
        return head
