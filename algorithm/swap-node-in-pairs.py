# Description: Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without 
# modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Input: head = []
# Output: []
# Input: head = [1]
# Output: [1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        pointer = head.next # new head
        temp = head
        pre_temp = None
        while temp and temp.next: # when exist a node pair, swap two nodes
            if pre_temp:
                pre_temp.next = temp.next  # reconnect between the pair
            # swap node pair
            end_pair = temp.next
            temp.next = end_pair.next
            end_pair.next = temp
            pre_temp = temp
            temp = temp.next
        
        return pointer
