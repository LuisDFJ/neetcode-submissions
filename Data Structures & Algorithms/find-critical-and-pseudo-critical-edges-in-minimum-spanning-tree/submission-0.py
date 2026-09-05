class UnionFind:
    def __init__(self,n:int):
        self.par = [i for i in range(n)]
        self.ran = [0 for _ in range(n)]
    def find(self,x:int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x),self.find(y)
        if a == b: return False
        if self.ran[a] < self.ran[b]: a,b = b,a
        self.par[b] = a
        self.ran[a] += 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i,e in enumerate(edges):
            e.append(i)
        edges.sort(key=lambda e:e[2])

        mst_weight = 0
        uf = UnionFind(n)
        for v1,v2,w,_ in edges:
            if uf.union(v1,v2): mst_weight += w
        
        critical,pseudo = [],[]
        for n1,n2,e_weight,i in edges:
            weight = 0
            uf = UnionFind(n)
            count = 0
            for v1,v2,w,j in edges:
                if i != j and uf.union(v1,v2):
                    weight += w
                    count += 1
            if count != n-1 or weight > mst_weight:
                critical.append(i)
                continue
            
            weight = e_weight
            uf = UnionFind(n)
            uf.union(n1,n2)
            for v1,v2,w,j in edges:
                if uf.union(v1,v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical,pseudo]
            


        