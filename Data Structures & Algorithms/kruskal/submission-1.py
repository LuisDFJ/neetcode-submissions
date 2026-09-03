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
        a,b= self.find(x),self.find(y)
        if a == b: return False
        if self.rank[a] < self.rank[b]:
            a,b = b,a
        self.parents[b] = a
        self.rank[a] += 1
        return True
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        heap = []
        for a,b,weight in edges:
            heapq.heappush(heap,(weight,a,b))

        uf = UnionFind(n)
        res = 0
        nodes = 0
        while heap and nodes < n-1:
            weight,a,b = heapq.heappop(heap)
            if not uf.union(a,b): continue
            res += weight
            nodes += 1
        return res if nodes == n-1 else -1
       

