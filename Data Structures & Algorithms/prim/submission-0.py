class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for src,dst,weight in edges:
            adj[src].append((weight,dst))
            adj[dst].append((weight,src))
        
        heap = []
        for weight,dst in adj[0]:
            heapq.heappush(heap,(weight,0,dst))
        visit = {0}
        res = []
        cost = 0
        while heap:
            weight,src,dst = heapq.heappop(heap)
            if dst in visit: continue
            visit.add(dst)
            res.append((src,dst))
            cost += weight
            for weight,node in adj[dst]:
                if node not in visit:
                    heapq.heappush(heap,(weight,dst,node))
        if len(res) == n-1: return cost
        return -1

        