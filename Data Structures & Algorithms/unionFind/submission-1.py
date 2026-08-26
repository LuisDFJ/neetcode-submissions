class UnionFind:
    def __init__(self, n: int):
        self.parent = {i:i for i in range(n)}
        self.rank = {i:0 for i in range(n)}

    def find(self, x: int) -> int:
        curr = self.parent[x]
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        a,b = self.find(x), self.find(y)
        if a == b: return False
        
        if self.rank[a] > self.rank[b]:
            self.parent[b] = a
        elif self.rank[a] < self.rank[b]:
            self.parent[a] = b
        else:
            self.parent[a] = b
            self.rank[b] += 1
        return True

    def getNumComponents(self) -> int:
        return sum([ 1 for k,v in self.parent.items() if k == v ])

