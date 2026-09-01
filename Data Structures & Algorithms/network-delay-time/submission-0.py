from heapq import heappop,heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1,n+1)}
        for source, dest, weight in times:
            adj[source].append((dest,weight))
        
        table = {}
        heap = [(0,k)]
        while heap:
            w1,n1 = heappop(heap)
            if n1 in table: continue
            table[n1] = w1
            for n2,w2 in adj[n1]:
                if n2 not in table:
                    heappush(heap,(w1+w2,n2))
        
        if len(table) != n: return -1
        maxTime = 0
        for _,time in table.items():
            maxTime = max(maxTime,time)
        return maxTime
