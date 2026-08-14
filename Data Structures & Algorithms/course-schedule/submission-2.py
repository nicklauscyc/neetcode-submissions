class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build an adj list with dictionary key map to set where key is the course and 
        # set are the pre-req
        # For each edge, check if there is a reverse relationship
        # If such a reverse relationship exists, output False
        # Else after iterating through everything, output True

        req = {}
        for p in prerequisites:
            course = p[0]
            pre = p[1]

            if pre in req:
                if course in req[pre]:
                    return False
            
            if course not in req:
                req[course] = set()

            req[course].add(pre)
        
        # Now we dfs and find any cycles
        def dfs(node, visited, path): 
            if node in path: 
                return False

            if node in visited:
                return True

            visited.add(node)
            path.add(node)

            # No neighbors
            if node not in req: 
                path.remove(node) # Update the path for backtracking
                return True

            for neigh in req[node]:
                if not dfs(neigh, visited, path):
                    path.remove(node) # Update the path for backtracking
                    return False

            path.remove(node) # Update the path for backtracking
            return True

        visited = set()
        for course in req:
            if course not in visited:
                visited.clear()
                path = set()
                if not dfs(course, visited, path):
                    return False
        return True