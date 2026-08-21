class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(i:int,j:int) -> int:
            if i == m or j == n: return 0
            if (i,j) in cache: return cache[(i,j)]
            if i == m-1 and j == n-1: return 1
            paths = 0
            paths += dfs(i+1,j)
            paths += dfs(i,j+1)
            cache[(i,j)] = paths
            return paths
        return dfs(0,0)