class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        M,N = len(grid), len(grid[0])
        #if gird[0][0] == 1 or grid[M-1][N-1] == 1: return 0

        prev = [0] * N
        prev[N-1] = 1

        for i in range(M-1,-1,-1):
            curr = [0] * N
            for j in range(N-1,-1,-1):
                if grid[i][j] == 1: curr[j] = 0
                elif j == N-1: curr[j] = prev[j]
                else: curr[j] = prev[j] + curr[j+1]
            prev = curr
        return prev[0]