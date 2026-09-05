class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        stack = set()
        for course in range(numCourses):
            if not dfs(course,adj,visit,stack): return False
        return True

def dfs(course:int, adj:dict, visit:set, stack:set) -> bool:
    if course in stack: return False
    if course in visit: return True
    stack.add(course)
    visit.add(course)
    for neighbor in adj[course]:
        if not dfs(neighbor,adj,visit,stack): return False
    stack.remove(course)
    return True