class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = {i:[] for i in range(n)}
        for source,dest,weight in edges:
            adj[source].append((dest,weight))
        
        heap = [(0,src)]
        table = {}
        while heap:
            w1,n1 = heapq.heappop(heap)
            if n1 in table: continue
            table[n1] = w1
            for n2,w2 in adj[n1]:
                if n2 not in table:
                    heapq.heappush(heap,(w1+w2,n2))
        for i in range(n):
            if i not in table:
                table[i] = -1
        return table

