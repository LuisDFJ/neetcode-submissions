class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        N,M = len(grid), len(grid[0])
        cache = {}
        def dfs(i : int, j : int) -> int:
            if i == N or j == M: return 0
            if grid[i][j] == 1: return 0
            if (i,j) in cache: return cache[(i,j)]
            if i == N-1 and j == M-1: return 1
            paths = 0
            paths += dfs(i+1,j)
            paths += dfs(i,j+1)
            cache[(i,j)] = paths
            return paths
        return dfs(0,0)


        