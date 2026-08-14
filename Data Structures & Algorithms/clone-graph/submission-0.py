"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def bfs(self, node, copy, visited, val2node):
        if not node:
            return 
        if node.val in visited: 
            return 
        visited.add(node.val)
        print("visited", node.val)

        res = [] # for debug
        for n in node.neighbors:
            print("neighbor", n.val)
            copy_n = None
            if n.val in val2node:
                copy_n = val2node[n.val] 
            else: 
                print("creating node for", n.val)
                copy_n = Node(n.val)
                val2node[n.val] = copy_n

            #copy_n = val2node.get(n.val, Node(n.val))

            copy.neighbors.append(copy_n)
            self.bfs(n, copy_n, visited, val2node)
            res.append(copy_n.val)
        if not res: 
            print(copy.val, "no neighbors")

        print(copy.val, res)
        return copy

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return
        val2node = {}
        visited = set()
        root_copy = Node(node.val)
        val2node[node.val] = root_copy
        print("creating node for", node.val)
        copy = self.bfs(node, root_copy, visited, val2node) 
        return copy

 

        