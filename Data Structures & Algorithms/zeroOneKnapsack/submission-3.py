class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M = len(profit),capacity
        mem = [[-1] * (M+1) for _ in range(N) ]
        return dfs(0,capacity,profit,weight,mem)

def dfs(i:int,c:int,profit:list,weight:list,mem:list[list[int]]) -> int:
    if i == len(profit): return 0
    if mem[i][c] != -1: return mem[i][c]
    mem[i][c] = dfs(i+1,c,profit,weight,mem)
    newCap = c - weight[i]
    if newCap >= 0:
        p = profit[i] + dfs(i+1,newCap,profit,weight,mem)
        mem[i][c] = max(mem[i][c],p)
    return mem[i][c]