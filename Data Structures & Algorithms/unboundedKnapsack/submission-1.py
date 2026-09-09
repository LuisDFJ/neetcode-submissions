class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        cache = {}
        def dfs(i:int,cap:int) -> int:
            if i == len(profit): return 0
            if (i,cap) in cache: return cache[(i,cap)]
            maxProfit = dfs(i+1,cap)
            newCap = cap - weight[i]
            if newCap >= 0:
                maxProfit = max(maxProfit,profit[i] + dfs(i,newCap))
            cache[(i,cap)] = maxProfit
            return maxProfit
        return dfs(0,capacity)
