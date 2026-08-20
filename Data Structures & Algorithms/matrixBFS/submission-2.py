from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        N,M = len(grid),len(grid[0])
        root = (0,0)
        target = (N-1,M-1)
        queue = deque([root])
        visit = set([root])

        def neighbors(r:int,c:int) -> Iterator[tuple[int,int]]:
            for i,j in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if i<0 or j<0 or i>=N or j>=M or grid[i][j]==1 or (i,j) in visit:
                    continue
                yield i,j

        length = 0
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                if (r,c) == target:
                    return length
                for i,j in neighbors(r,c):
                    visit.add((i,j))
                    queue.append((i,j))
            length += 1
        return -1

        