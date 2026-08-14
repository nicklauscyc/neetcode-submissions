# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Needed tutorial to do this, 14 mins to implement.
# Observe the position of the root in the preorder array
# Observe how the position of the root partitions the in order array into left and right subtrees
# array positions imply the recursive structure of L-subtree, root, R-subtree
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        # Base case
        if not preorder:
            return None

        root = preorder[0]
        if len(preorder) == 1:
            return TreeNode(root)

    
        m = inorder.index(root)
        root_node = TreeNode(root)


        left_inord = inorder[0:m]
        right_inord = inorder[m+1:]
        left_preord = preorder[1:1+len(left_inord)]
        right_preord = preorder[1+len(left_inord):]

        #print(left_preord, left_inord)
        #print(right_preord, right_inord)

        left_tree = self.buildTree(left_preord, left_inord)
        right_tree = self.buildTree(right_preord, right_inord)
        root_node.left = left_tree
        root_node.right = right_tree

        return root_node

       

        