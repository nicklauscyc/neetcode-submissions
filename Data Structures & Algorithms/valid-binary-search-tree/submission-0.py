# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def check(node, lowerBound, upperBound):
            if not node:
                return True
            
            # Check if immediate child and parent relationships
            if node.left and node.left.val >= node.val: 
                    return False

            if node.right and node.val >= node.right.val: 
                    return False
            
            # Check bounds of the trio
            if node.right and node.right.val >= upperBound: 
                return False
            
            if node.left and node.left.val <= lowerBound: 
                return False
            
            return check(node.left, lowerBound, node.val) and check(node.right, node.val, upperBound)
        
        return check(root, -1001, 1001)
        