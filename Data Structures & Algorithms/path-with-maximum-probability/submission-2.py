class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = { i:[] for i in range(n) }
        for (start,end),prob in zip(edges,succProb):
            adj[start].append((prob,end))
            adj[end].append((prob,start))
        
        table = set()
        heap = [(-1.0,start_node)]
        while heap:
            p1,n1 = heapq.heappop(heap)
            if n1 in table: continue
            if n1 == end_node: return -p1
            table.add(n1)
            for p2,n2 in adj[n1]:
                if n2 not in table:
                    heapq.heappush(heap,(p1*p2,n2))
        return 0.0
        