# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, node, res):
        if not node: 
            return 
        
        self.dfs(node.left, res)

        if node.left:
            res.append(str(node.left.val))
        else: 
            res.append("n")

        res.append(str(node.val))
        if node.right:
            res.append(str(node.right.val))
        else: 
            res.append("n")
        
        self.dfs(node.right, res)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = []
        self.dfs(root, res)
        
        str_res = "".join(res)
        print(str(str_res))
        

        s_res = []
        self.dfs(subRoot, s_res)
      
        str_s_res = "".join(s_res)
        print(str(str_s_res))

        for j in range(len(str_res)):
            match = False
            i = 0 # substring
            while i < len(str_s_res) and j < len(str_res):
                if str_s_res[i] != str_res[j]:
                    break
                i += 1
                j += 1
            if i == len(str_s_res):
                return True
                        

        return False
        