# Observe that the in-ord traversal with the null leaves uniquely identify a tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def dfs(self, node, arr):
        if not node:
            arr.append('null')
            return 
        arr.append(str(node.val))
        self.dfs(node.left, arr)
        self.dfs(node.right, arr)

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        self.dfs(root, arr)
        res = ','.join(arr)
        print(res)
        return res
     
    def build(self, arr, i):
        if i >= len(arr):
            return (None, i)
        if arr[i] == 'null':
            return (None, i+1)
        
        node = TreeNode(int(arr[i]))

        left, i = self.build(arr, i+1)
        right, i = self.build(arr, i)
        node.left = left
        node.right = right
        return (node, i)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split(',')
        root, i = self.build(arr, 0)
        return root

