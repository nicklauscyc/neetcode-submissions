from collections import deque
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Implemented with a topological sort

        # Build the graph
        G = [[] for i in range(len(numCourses))]
        for course, prereq in prerequisites: 
            G[course].append(prereq)

        # Find the first course that has no pre-req to begin our search 
        topSorted = [] # For debug purposes
        coursesWithNoPrereq= deque() 
        for course in G: 
            if not course:
                coursesWithNoPrereq.append(course)
        
        finish = 0
        while coursesWithNoPrereq: 
            course = coursesWithNoPrereq.popleft()
            finish += 1 
            for prereq in G[course]: 
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses


        