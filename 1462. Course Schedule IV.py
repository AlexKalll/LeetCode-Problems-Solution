# https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def isPrerequisite(self, adjlist, visited, src, target):
        visited[src] = True
        if src == target:
            return True
        for adj in adjlist.get(src, []):
            if not visited[adj]:
                if self.isPrerequisite(adjlist, visited, adj, target):
                    return True
        return False

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjlist = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adjlist[a].append(b)
        
        ans = []

        for u, v in queries:
            visited = [False] * numCourses
            ans.append(self.isPrerequisite(adjlist, visited, u, v))

        return ans
        
