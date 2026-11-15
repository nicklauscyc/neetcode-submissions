class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comps = [] # List of sets of components, each component is a set for quick lookup
        # worst case it's n squared where n is number of vertices
        
        G = {}
        for a in range(n):
            G[a] = set()

        for (a, b) in edges:
            if not a in G:
                G[a] = set()
            if not b in G:
                G[b] = set()
            G[a].add(b)
            G[b].add(a)
            
        #for g in G:
        #    print(g, "->", G[g])

        def dfs(node, visited):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in G[node]:
                dfs(neighbor, visited)
        
        all_disjoint = []
        for v in G:
            # Test if v is in one of our unions
            vFound = False
            for union in all_disjoint:
                if v in union:
                    vFound = True
                    break
            if vFound:
                continue
                  
            # v will be a new union, let's DFS again
            visited = set()
            dfs(v, visited)
            all_disjoint.append(visited)
            #print(all_disjoint)          
        
        return len(all_disjoint)