from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses, p):
        toposort = []
        queue = deque()
        AList = defaultdict(list)
        indegree = defaultdict(lambda:0)
        for edge in p:
            indegree[edge[0]]+=1
            AList[edge[1]].append(edge[0])
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        while len(queue)>0:
            curr = queue.popleft()
            toposort.append(curr)
            for nodes in AList[curr]:
                indegree[nodes]-=1
                if indegree[nodes]==0:
                    queue.append(nodes)
        return toposort if len(toposort)==numCourses else []

s = Solution()
numCourses = 2
prerequisites = [[0, 1]]
r = s.findOrder(numCourses, prerequisites)
print(r)