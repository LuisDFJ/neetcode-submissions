from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        N,M = len(grid),len(grid[0])
        queue = deque( [(i,j) for i in range(N) for j in range(M) if grid[i][j]== 2] )
        visit = { (i,j) for i in range(N) for j in range(M) if grid[i][j]!=1 }
        fresh = sum(1 for i in range(N) for j in range(M) if grid[i][j]==1)

        def neighbors(i: int, j: int) -> Iterator[tuple[int,int]]:
            for n,m in [(i-1,j),(i,j+1),(i+1,j),(i,j-1)]:
                if 0<=n<N and 0<=m<M and (n,m) not in visit:
                    yield n,m

        level = 0
        while queue and fresh > 0:
            for _ in range(len(queue)):
                i,j = queue.popleft()
                for n in neighbors(i,j):
                    visit.add(n)
                    queue.append(n)
                    fresh -= 1
            level += 1
        
        return level if fresh == 0 else -1


        