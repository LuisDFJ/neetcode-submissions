class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit),capacity
        prev = [ 0 if weight[0] > cap else profit[0] for cap in range(M+1) ]
        for i in range(1,N):
            curr = [ 0 ] * (M+1)
            for cap in range(1,M+1):
                include = 0
                if cap - weight[i] >= 0:
                    include = profit[i] + prev[cap-weight[i]]
                curr[cap] = max(prev[cap],include)
            prev = curr
        return prev[-1]
