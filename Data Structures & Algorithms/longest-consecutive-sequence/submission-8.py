class UnionFind:
    def __init__(self,nums:List[int]):
        self.par = {n:n for n in nums}
        self.rank = {n:1 for n in nums}
        self.maxRank = 1
    def find(self,x:int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x), self.find(y)
        if a == b: return False
        if self.rank[a] < self.rank[b]:
            a,b = b,a
        self.par[b] = a
        self.rank[a] += self.rank[b]
        self.maxRank = max(self.maxRank, self.rank[a])
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        uf = UnionFind(nums)
        s = set(nums)
        for n in nums:
            if n-1 in s:
                uf.union(n,n-1)
        return uf.maxRank