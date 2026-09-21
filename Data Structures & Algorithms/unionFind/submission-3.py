class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        a,b = self.find(x), self.find(y)
        if a == b: return False
        if self.rank[a] < self.rank[b]:
            a,b = b,a
        self.parent[b] = a
        self.rank[a] += self.rank[b]
        return True

    def getNumComponents(self) -> int:
        return sum( i == v for i,v in enumerate(self.parent) )