# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.negInf = -1001
        self.maxPath = self.negInf
        self.dfs(root)
        return self.maxPath

    def dfs(self, node):
       
        if not node: 
            return self.negInf
      

        leftSum = self.dfs(node.left)
        rightSum = self.dfs(node.right)
 

        # Check what happens if we end here
        bendSum = leftSum + node.val + rightSum
        maxSumHere = max(leftSum, leftSum + node.val, rightSum, rightSum + node.val, bendSum, node.val)
        if maxSumHere > self.maxPath:
            self.maxPath = maxSumHere
 

        return max(leftSum + node.val, rightSum + node.val, node.val)
