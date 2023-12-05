# Description: Given the head of a linked list, return the node where 
# the cycle begins. If there is no cycle, return null.
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        pointer1 = head
        pointer2 = head
        pointer3 = head
        if pointer1.next:
            while pointer2.next:
                pointer1 = pointer1.next
                pointer2 = pointer2.next.next
                if pointer2 is None or pointer1 == pointer2: # meet or not a cycle
                    break
            
            if pointer2 is None or pointer2.next is None:
                return None
            
            # notice: if p1 meet p2, they met at position km - l. m is the cycle's length and l is
            # the length outside the cycle. k is an integer. 
            # move a new pointer until it enter the loop after l steps (condition: p1 = p3)
            while pointer1 != pointer3:
                pointer1 = pointer1.next
                pointer3 = pointer3.next
            
            return pointer3
        else:
            return None
        