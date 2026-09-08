def count(word:str,c:str) -> int:
    return sum( s==c for s in word)
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        weight = [ (count(word,"0"), count(word,"1"))for word in strs ]
        mem = {}
        def dfs( i:int, m:int, n:int ) -> int:
            if i == N: return 0
            if (i,m,n) in mem: return mem[(i,m,n)]
            newM = m - weight[i][0]
            newN = n - weight[i][1]
            maxProfit = dfs(i+1,m,n)
            if newM >=0 and newN >=0:
                maxProfit = max( maxProfit, 1 + dfs(i+1,newM,newN) )
            mem[(i,m,n)] = maxProfit
            return maxProfit
        return dfs(0,m,n)
        