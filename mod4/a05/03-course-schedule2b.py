class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q=deque()
        c=0
        if numCourses<=1:
            return [i for i in range(numCourses)]
        indeg=[0]*numCourses
        graph=[[] for _ in range(numCourses)]
        for s1,s2 in prerequisites:
            graph[s2].append(s1)
            indeg[s1]+=1
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        res=[]
        while q:
            course=q.popleft()
            res.append(course)
            c+=1
            for child in graph[course]:
                indeg[child]-=1
                if indeg[child]==0:
                    q.append(child)

        if c==numCourses:
            return res
        return []

