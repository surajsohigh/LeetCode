# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize carry and dummy node to build the resulting linked list
        carry = 0
        dummy = ListNode()
        current = dummy

        # Traverse both lists
        while l1 or l2 or carry:
            # If a list is exhausted, use 0 as its value
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum of two nodes and carry
            sumVal = val1 + val2 + carry
            carry = sumVal // 10  # Update carry for next iteration
            current.next = ListNode(sumVal % 10)  # Create new node for the sum's remainder
            current = current.next
            
            # Move to the next node in both lists if available
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next  # Return the next node of the dummy, which is the result list
