from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # construct graph and get indegrees for every index/course
        graph = defaultdict(list)
        indegrees = [0]*numCourses
        for p in prerequisites:
            graph[p[0]].append(p[1])
            indegrees[p[1]] += 1

        # get initial list of indices/courses to visit
        queue = deque()
        processed = 0
        for i, x in enumerate(indegrees):
            if not x:
                queue.append(i)

        # conduct topological sort
        while queue:
            course = queue.popleft()
            processed += 1
            for c in graph[course]:
                indegrees[c] -= 1
                if not indegrees[c]:
                    queue.append(c)

        return processed == numCourses

s = Solution()
numCourses = 2
prerequisites = [[0, 1]]
r = s.canFinish(numCourses, prerequisites)
print(r)