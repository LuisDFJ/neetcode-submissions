class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
        
        visit = set()
        path = set()
        res = []
        for course in range(numCourses):
            if not dfs(course,adj,visit,path,res): return []
        return res

def dfs(course:int,adj:dict,visit:set,path:set,res:list) -> bool:
    if course in path: return False
    if course in visit: return True
    visit.add(course)
    path.add(course)
    for neighbor in adj[course]:
        if not dfs(neighbor,adj,visit,path,res): return False
    path.remove(course)
    res.append(course)
    return True
        