class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                p,q = points[i],points[j]
                w = abs(p[0]-q[0]) + abs(p[1]-q[1])
                adj[i].append( (w,j) )
                adj[j].append( (w,i) )
        
        visit = {0}
        heap = []
        for w,node in adj[0]:
            heapq.heappush(heap,(w,0,node))
        cost = 0
        while heap:
            weight,src,dst = heapq.heappop(heap)
            if dst in visit: continue
            visit.add(dst)
            cost += weight
            for weight,node in adj[dst]:
                if node not in visit:
                    heapq.heappush(heap,(weight,dst,node))
        return cost


        