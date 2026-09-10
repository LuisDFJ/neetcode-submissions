class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mem = {}
        def dfs(i:int,j:int) -> int:
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i,j) in mem: return mem[(i,j)]
            res = 0
            if word1[i] == word2[j]:
                res = dfs(i+1,j+1)
            else:
                res = 1 + min( dfs(i+1,j+1), dfs(i,j+1), dfs(i+1,j) )
            mem[(i,j)] = res
            return res
        return dfs(0,0)