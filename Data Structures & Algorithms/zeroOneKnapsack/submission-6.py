class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit),capacity
        mem = [[0] * (M+1) for _ in range(N) ]
        for cap in range(1,M+1):
            if cap >= weight[0]: mem[0][cap] = profit[0]
        
        for i in range(1,N):
            for cap in range(1,M+1):
                newProfit = 0
                if cap - weight[i] >= 0:
                    newProfit = profit[i] + mem[i-1][cap-weight[i]]
                mem[i][cap] = max(mem[i-1][cap],newProfit)
        return mem[N-1][M]
