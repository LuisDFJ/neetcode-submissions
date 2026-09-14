class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        mem = {}
        def dfs(l:int,r:int,s:str) -> int:
            if l < 0 or r == len(s):
                return 0
            if (l,r) in mem: return mem[(l,r)]
            res = 0
            if s[l] == s[r]:
                res = dfs(l-1,r+1,s) + (1 if l==r else 2)
            else:
                res = max(dfs(l,r+1,s), dfs(l-1,r,s))
            mem[(l,r)] = res
            return res
            
        res = 0
        for i in range(len(s)):
            res = max(res,dfs(i,i,s))
            res = max(res,dfs(i,i+1,s))
        return res

        

