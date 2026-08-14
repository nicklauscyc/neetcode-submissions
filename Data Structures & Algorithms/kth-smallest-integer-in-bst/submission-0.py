# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node, k, seen):
            print(seen)
            if not node:
                return 
            
            l = dfs(node.left, k, seen)
            if l:
                return l
            seen.append(node.val)
            print("after append", node.val, seen, len(seen), k)
            if len(seen) == k:
                "print len seen!"
                return node.val
            r = dfs(node.right, k, seen)
            if r:
                return r
        
        res = dfs(root, k, [])
        print(res)
        return res

        