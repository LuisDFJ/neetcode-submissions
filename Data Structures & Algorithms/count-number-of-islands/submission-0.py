class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        N,M = len(grid),len(grid[0])
        def flood(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= N or c >= M  or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for n,m in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                flood(n,m)
        
        islands = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    islands += 1
                    flood(i,j)
        return islands

            