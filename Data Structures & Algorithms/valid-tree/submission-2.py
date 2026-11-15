class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        # Basically just cycle detection
        # 5 min so far
        tree = {}
        for edge in edges:
            a = edge[0]
            b = edge[1]
            if a not in tree:
                tree[a] = set()
            if b not in tree:
                tree[b] = set()
            tree[a].add(b)
            tree[b].add(a)
        
        #for n in tree:
        #   print(n, tree[n])

        # Return False if has cycle, True otherwise
        def dfs(node, visited, stack):
            if node in visited:
                if len(stack) >= 2 and stack[-2] != node:
                    #print("ret false in dfs, node", node, stack)
                    return False # has cycle
                return True

            stack.append(node)
            visited.add(node)
            for n in tree[node]:
                test = dfs(n, visited, stack)
                if not test:
                    stack.pop()
                    return False
            stack.pop()
            return True
        
        for n in tree:
            visited = set()
            stack = []
            test = dfs(n, visited, stack)
            if not test:
                #print(n, "ret false")
                return False
        return True
            

        

            
        