class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = { c : [] for c in range(numCourses) }
        for a,b in prerequisites:
            graph[a].append(b)

        visit = set()
        def dfs( root: int ) -> bool:
            if root in visit:
                return False
            if not graph[root]:
                return True
            
            visit.add(root)
            for neighbor in graph[root]:
                if not dfs(neighbor):
                    return False
            visit.remove(root)
            graph[root] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c): return False
        return True


        