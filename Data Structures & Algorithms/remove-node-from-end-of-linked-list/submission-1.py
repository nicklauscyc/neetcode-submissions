# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def printList(self, head):
        curr = head
        l = []
        while curr:
            l.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(l))

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head
        while curr:
            N += 1
            curr = curr.next
        
        delete_index = N - n

        i = 0
        curr = head
        prev = None
        print("delete_index", delete_index)
        while curr:
            print("curr.val", curr.val)
            if i == delete_index:
                if i == 0:
                    head = curr.next
                else:
                    prev.next = curr.next
                curr.next = None
            prev = curr
            curr = curr.next
            i += 1
        self.printList(head)
        return head

        