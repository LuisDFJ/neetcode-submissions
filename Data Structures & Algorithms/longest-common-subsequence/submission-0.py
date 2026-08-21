class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N,M = len(text1), len(text2)
        cache = {}
        def dfs( i : int, j : int ) -> int:
            if i == N or j == M: return 0
            if (i,j) in cache: return cache[(i,j)]
            if text1[i] == text2[j]:
                return 1 + dfs(i+1,j+1)
            accum = max(dfs(i+1,j),dfs(i,j+1))
            cache[(i,j)] = accum
            return accum
        return dfs(0,0)