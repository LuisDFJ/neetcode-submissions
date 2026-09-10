class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}
        def dfs(i:int,j:int) -> int:
            if j == len(t): return 1
            if i == len(s): return 0
            if (i,j) in mem: return mem[(i,j)]
            res = dfs(i+1,j)
            if s[i] == t[j]:
                res += dfs(i+1,j+1)
            mem[(i,j)] = res
            return res
        return dfs(0,0)
