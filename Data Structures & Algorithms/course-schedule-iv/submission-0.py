class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for src,dst in prerequisites:
            adj[src].append(dst)
        
        res = {i:set() for i in range(numCourses)}
        for course in range(numCourses):
            dfs(course,adj,set(),res)
        return [ dst in res[src] for src,dst in queries ]

def dfs(course:int,adj:dict,visit:set,res:dict):
    if course in visit: return
    visit.add(course)
    for neighbor in adj[course]:
        dfs(neighbor,adj,visit,res)
        res[course].add(neighbor)
    for neighbor in adj[course]:
        for n in res[neighbor]:
            res[course].add(n)
