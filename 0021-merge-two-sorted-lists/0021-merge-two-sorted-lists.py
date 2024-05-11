# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
#         i=0
#         j=0
        
#         while i<len(list1) and j<len(list2):
#             if list1[i]>list2[j]:
        
        temp = list1
        temp2=list2
        
        dummy = ListNode(-1)
        current = dummy
                
        while list1 and list2:
            
            if list1.val >= list2.val:
                current.next = list2
                list2=list2.next
            else:
                current.next = list1
                list1=list1.next
                
            current = current.next
            
        
            
        while list1:
            print("h",list1.val)
            current.next = list1
            list1 = list1.next
            current = current.next
            
        while list2:
            print("yh",list2.val, current.val)
            
            current.next = list2
            list2 = list2.next
            current = current.next
            
        
        return dummy.next