# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        root = None
        p1 = None
        p2 = None
        if list1.val < list2.val:
            root = list1
            p1 = root.next
            p2 = list2
        else:
            root = list2
            p2 = list2.next
            p1 = list1
        
        curr = root
        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                curr = p1
                p1 = p1.next
            else:
                curr.next = p2
                curr = p2
                p2 = p2.next

        while p1:
            curr.next = p1
            curr = p1
            p1 = p1.next
        
        while p2:
            curr.next = p2
            curr = p2
            p2 = p2.next
        
        return root


        
        
    
        