class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        N,M = len(grid), len(grid[0])
        visit = set()
        def neighbors(r: int, c: int) -> Iterator[tuple[int,int]]:
            nonlocal grid,visit
            if grid[r][c] == 0:
                for n,m in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                    if (n,m) not in visit and min(n,m) >= 0 and n < N and m < M and grid[n][m] == 0:
                        yield n,m

        target = (N-1,M-1)
        def dfs(r : int, c : int) -> int:
            nonlocal grid, visit, target
            if (r,c) == target:
                return 1
            visit.add((r,c))
            res = 0
            for n,m in neighbors(r,c):
                res += dfs(n,m)
            visit.remove((r,c))
            return res
        
        return dfs(0,0)

        