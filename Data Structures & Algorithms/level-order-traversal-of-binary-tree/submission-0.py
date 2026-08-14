
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node, level, items):
        if not node: 
            return 
        self.dfs(node.left, level+1, items)
        
        if level in items:
            items[level].append(node.val)
        else:
            items[level] = [node.val]

        self.dfs(node.right, level+1, items)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        items = {}
        self.dfs(root, 0, items)
        print(items) 

        level = 0
        res = []
        while level in items:
            res.append(items[level])
            level += 1
        return res

        