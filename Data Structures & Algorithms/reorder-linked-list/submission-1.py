# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Insight is to reverse the 2nd half of the list

    def printList(self, head):
        curr = head
        s = []
        while curr:
            s.append(str(curr.val))
            curr = curr.next
            
        print(" -> ".join(s))

    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        head = prev
        return head
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Find the middle
        slow = head
        fast = head
        prev_slow = None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        # Break into 2 lists
        if prev_slow:
            prev_slow.next = None

        # Reverse the second half
        slow_head = self.reverseList(slow)

        self.printList(head)
        self.printList(slow_head)


        # Interleaving step
        real_head = head
    
        while real_head:
            # Invariant is that real_head => slow_head not None
            save = real_head.next
            save_slow = slow_head.next

            real_head.next = slow_head
            real_head = save

            slow_head.next = real_head

            prev = slow_head
            slow_head = save_slow
            print("real_head", real_head.val if real_head else None, \
            "slow_head", slow_head.val if slow_head else None)

        if slow_head:
            prev.next = slow_head
        
        self.printList(head)

        