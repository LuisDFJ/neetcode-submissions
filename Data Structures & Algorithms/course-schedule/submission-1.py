class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { course : [] for course in range(numCourses) }
        for a,b in prerequisites:
            graph[a].append(b)
        
        visit = set()

        def dfs( node : int ) -> bool:
            if node in visit: return False
            if not graph[node]: return True

            visit.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor): return False
            visit.remove(node)
            graph[node] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True