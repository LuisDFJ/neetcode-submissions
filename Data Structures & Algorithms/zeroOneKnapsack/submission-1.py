class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return dfs(0,capacity,profit,weight,{})

    
def dfs(i:int,cap:int,profit:list,weight:list,mem:dict) -> int:
    if (i,cap) in mem: return mem[(i,cap)]
    if i == len(profit): return 0
    mem[(i,cap)] = dfs(i+1,cap,profit,weight,mem)
    newCap = cap - weight[i]
    if newCap >= 0:
        p = profit[i] + dfs(i+1,newCap,profit,weight,mem)
        mem[(i,cap)] = max(mem[(i,cap)],p)
    return mem[(i,cap)]
