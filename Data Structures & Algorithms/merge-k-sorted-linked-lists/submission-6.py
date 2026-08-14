# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 28 mins
# sigh you need to do merge sort way. Zip pairs together
class Solution:    
    def zip(self, list1, list2):
        head = None
        curr = None
        while list1 and list2:
            small = None
            if list2.val < list1.val:
                small = list2
                list2 = list2.next
            else:
                small = list1
                list1 = list1.next
            
            if not head:
                head = small
            else:
                curr.next = small
            curr = small
        while list1:
            curr.next = list1
            curr = list1
            list1 = list1.next
        while list2:
            curr.next = list2
            curr = list2
            list2 = list2.next
        return head

    def printList(self, node):
        arr = []
        while node:
            if node:
                arr.append(node.val)
                node = node.next
        print(arr)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        temp = lists
        count = 0
        while len(temp) > 1:
        
            for i in range(len(temp)):
                self.printList(temp[i])
            
            if count > 10:
                break
            merged = []
            for i in range(0,len(temp),2):
                j = i+1
                #print("i, j", i, j)
                if j >= len(temp):
                    merged.append(temp[i])
                else:
                    zipped = self.zip(temp[i], temp[j])
                    merged.append(zipped)
            temp = merged
            count += 1

        
        return temp[0] if temp else None


