class UnionFind:
    def __init__(self,n:int):
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self,x:int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x),self.find(y)
        if a==b: return False
        if self.rank[a] < self.rank[b]: a,b = b,a
        self.parents[b] = a
        self.rank[a] += 1
        return True
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = []
        for i in range(n):
            for j in range(i+1,n):
                a,b = points[i],points[j]
                w = abs(a[0]-b[0]) + abs(a[1]-b[1])
                heapq.heappush(heap,(w,i,j))
        
        uf = UnionFind(n)
        res = 0
        count = 0
        while count < n-1:
            w,i,j = heapq.heappop(heap)
            if not uf.union(i,j): continue
            res += w
            count += 1
        return res
        