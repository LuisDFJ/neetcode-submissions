class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return cached(text1,text2)(0,0)

def cached(a:str,b:str):
    mem = {}
    def dfs(i:int,j:int) -> int:
        if i == len(a) or j == len(b): return 0
        if (i,j) in mem: return mem[(i,j)]
        res = 0
        if a[i] == b[j]:
            res = 1 + dfs(i+1,j+1)
        else:
            res = max(dfs(i+1,j), dfs(i,j+1))
        mem[(i,j)] = res
        return res
    return dfs

