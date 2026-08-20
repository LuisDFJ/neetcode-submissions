from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        origin = (0,0)
        target = (N-1,N-1)
        if grid[0][0] == 1 or grid[N-1][N-1] == 1: return -1
        visit = set([origin])
        queue = deque([origin])

        def neighbors(row:int,col:int) -> Iterator[tuple[int,int]]:
            for i,j in [(row-1,col),(row+1,col),(row,col-1),(row,col+1),(row+1,col+1),(row+1,col-1),(row-1,col+1),(row-1,col-1)]:
                if 0 <= i < N and 0<=j<N and grid[i][j] == 0 and (i,j) not in visit:
                    yield i,j

        length = 1
        while queue:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                if (row,col) == target:
                    return length
                for i,j in neighbors(row,col):
                    visit.add((i,j))
                    queue.append((i,j))
            length += 1
        return -1
