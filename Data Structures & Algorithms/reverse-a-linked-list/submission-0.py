# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, prev, curr):
        print(curr.val)
        if not curr.next:
            # Base case
            self.head = curr
        else: 
            self.reverse(curr, curr.next)
        curr.next = prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        self.head = head
        self.reverse(None, head)
        return self.head
        