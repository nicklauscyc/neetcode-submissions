# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def Print(self, ancestors):
        s = ""
        for a in ancestors:
            s += str(a.val)
            s += ","
        print(s)
        
    def dfs(self, search, node, ancestors):
        # Returns a list of ancestors for search of type TreeNode
        #self.Print(ancestors)
        if not node:
            return False
        if node.val == search.val:
            ancestors.append(node)
            return True

        else:
            ancestors.append(node)
            l = self.dfs(search, node.left, ancestors)
            if l:
                return True
            r = self.dfs(search, node.right, ancestors)
            if r:
                return True
            ancestors.pop()
            return False

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        P = []
        Q = []
        self.dfs(p, root, P)
        self.dfs(q, root, Q)
        print(P)
        print(Q)
        ancestor = root
        for i in range(min(len(P), len(Q))):
            if P[i] == Q[i]:
                ancestor = Q[i]
        return ancestor
        