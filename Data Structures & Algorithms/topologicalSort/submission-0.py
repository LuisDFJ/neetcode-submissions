class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(n)}
        for src,dst in edges:
            adj[src].append(dst)
        
        res = []
        visit = set()
        stack = set()
        
        for node in range(n):
            if not dfs(node,adj,visit,stack,res): return []
        res.reverse()
        return res
    
def dfs(node:int,adj:dict[int,list[int]],visit:set[int],stack:set[int],res:list[int]) -> bool:
    if node in stack: return False
    if node in visit: return True
    stack.add(node)
    visit.add(node)
    for neighbor in adj[node]:
        if not dfs(neighbor,adj,visit,stack,res): return False
    stack.remove(node)
    res.append(node)
    return True