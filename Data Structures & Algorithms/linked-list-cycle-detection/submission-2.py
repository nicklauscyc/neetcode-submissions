# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()

        curr = head
        while curr:
            print("curr.val", curr.val)
            if curr in seen:
                print(curr.val, "seen")
                return True
            print("add", curr, "to seen")
            seen.add(curr)
            curr = curr.next
        return False
        