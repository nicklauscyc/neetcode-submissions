# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 28 mins
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)

        # Initialize array of k pointers to the start of each linked list
        ptrs = [lists[i] for i in range(k)]
        if not ptrs:
            return None

        finished = set() # set of indices i in ptrs that have iterated to the last element
        res = None
        curr = res
        while len(finished) < k:
            next_node = None
            next_index = 0

            for i in range(k):
                node = ptrs[i]
                if not node:
                    finished.add(i)
                    continue
                if not next_node:
                    next_node = node
                    next_index = i
                else:
                    if node.val < next_node.val:
                        next_node = node
                        next_index = i
            # Ok now we have picked the next node

            # If this is our first node, just assign it
            if not res:
                res = next_node
            else:
                curr.next = next_node
            curr = next_node
            #print(curr.val if curr else "None", len(finished), [ptrs[j].val if ptrs[j] else "None" for j in range(k)])
            ptrs[next_index] = ptrs[next_index].next if ptrs[next_index] else None
        return res


