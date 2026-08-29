class UnionFind:
    def __init__(self,nums:List[int]) -> None:
        self.par = {n:n for n in nums}
        self.ran = {n:1 for n in nums}
        self.rank_max = 1
    def find(self,x:int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x
    def union(self,x:int,y:int) -> bool:
        a,b = self.find(x),self.find(y)
        if a==b: return False
        if self.ran[a] < self.ran[b]:
            a,b = b,a
        self.par[b] = a
        self.ran[a] += self.ran[b]
        self.rank_max = max(self.rank_max,self.ran[a])
        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        snums = set(nums)
        uf = UnionFind(nums)
        for n in nums:
            if n-1 in snums:
                uf.union(n,n-1)
            elif n+1 in snums:
                uf.union(n,n+1)
        return uf.rank_max

                