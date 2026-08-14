# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def inv(node):
            if not root:
                return 
            swap = node.left
            node.left = node.right 
            node.right = swap
            self.invertTree(node.left)
            self.invertTree(node.right)
            return
        
        inv(root)
        return root