class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        totalWeight = sum(stones)
        target = (totalWeight+1)//2
        mem = {}
        def dfs(i:int,total:int):
            if total >= target or i == len(stones):
                return abs(total - (totalWeight - total))
            if (i,total) in mem: return mem[(i,total)]
            res =  min(dfs(i+1,total), dfs(i+1,total+stones[i]))
            mem[(i,total)] = res
            return res
        return dfs(0,0)