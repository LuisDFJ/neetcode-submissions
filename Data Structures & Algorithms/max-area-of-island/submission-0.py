class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        def dfs(row:int, col:int, visit:set) -> int:
            if row<0 or col<0 or row>=N or col >=M or grid[row][col] == 0 or (row,col) in visit:
                return 0
            visit.add((row,col))
            area = 1
            for i,j in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                area += dfs(i,j,visit)
            return area

        visit = set()
        res = 0
        for i in range(N):
            for j in range(M):
                if (i,j) not in visit:
                    res = max(res,dfs(i,j,visit))
        return res

            
        