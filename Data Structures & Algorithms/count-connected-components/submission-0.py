class UnionFind:
    def __init__(self,n:int) -> None:
        self.par = [i for i in range(n)]
        self.ran = [0 for _ in range(n)]
        self.n_graphs = n
    def find(self,x:int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x),self.find(y)
        if a == b: return False
        self.n_graphs -= 1
        if self.ran[a] < self.ran[b]:
            self.par[a] = b
        elif self.ran[a] > self.ran[b]:
            self.par[b] = a
        else:
            self.par[a] = b
            self.ran[b] += 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0],edge[1])
        return uf.n_graphs
        