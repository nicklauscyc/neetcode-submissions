from collections import deque

class Solution:
    # 30 min
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Implemented with a topological sort

        # Build the graph
        G = [set() for i in range(numCourses)]
        Prereq2Course = [set() for i in range(numCourses)]
        for course, prereq in prerequisites: 
            G[course].add(prereq) # prereq -> course

            Prereq2Course[prereq].add(course)

        # Find the first course that has no pre-req to begin our search 
        topSorted = [] # For debug purposes
        coursesWithNoPrereq = deque() 
        for i in range(len(G)): 
            if not G[i]: # if emptyset
                coursesWithNoPrereq.append(i)
        
        finish = 0
        while coursesWithNoPrereq: 
            course = coursesWithNoPrereq.popleft()
            finish += 1 
            topSorted.append(course)
            nextCourses = Prereq2Course[course]
            for nextCourse in nextCourses:
                G[nextCourse].remove(course) # Remove its prereq
                if not G[nextCourse]:
                    coursesWithNoPrereq.append(nextCourse)
        
        print(topSorted)
        return finish == numCourses



        