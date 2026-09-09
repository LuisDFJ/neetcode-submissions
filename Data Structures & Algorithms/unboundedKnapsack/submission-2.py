class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit),capacity
        prev = [0] * (M+1)
        for cap in range(1,M+1):
            idx = cap - weight[0]
            if idx >= 0:
                prev[cap] = profit[0] + prev[idx]
        
        for item in range(1,N):
            curr = prev.copy()
            for cap in range(1,M+1):
                idx = cap - weight[item]
                if idx >= 0:
                    curr[cap] = max(curr[cap], profit[item] + curr[idx])
            prev = curr
        return prev[-1]

