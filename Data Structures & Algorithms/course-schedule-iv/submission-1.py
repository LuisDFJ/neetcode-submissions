class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
        
        res = {}
        for course in range(numCourses):
            dfs(course,adj,res)
        return [ dst in res[src] for src,dst in queries ]

def dfs(course:int,adj:dict,visit:dict) -> set:
    if course in visit: return visit[course]
    visit[course] = set()
    for neighbor in adj[course]:
        visit[course].add(neighbor)
        visit[course] |= dfs(neighbor,adj,visit)
    return visit[course]
