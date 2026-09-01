def neighborsGenerator(grid: List[List[int]], visit: set[tuple[int,int]]):
    N,M = len(grid),len(grid[0])
    def wrapper(i:int,j:int) -> Iterator[tuple[tuple[int,int],int]]:
        for n,m in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= n < N and 0 <= m < M and (n,m) not in visit:
                yield (n,m),grid[n][m]
    return wrapper

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        neighbors = neighborsGenerator(grid,visited)
        heap = [(grid[0][0],(0,0))]
        target = (len(grid)-1, len(grid[0])-1)
        while heap:
            w1,n1 = heapq.heappop(heap)
            if n1 in visited: continue
            if n1 == target: return w1
            visited.add(n1)
            for n2,w2 in neighbors(n1[0],n1[1]):
                if n2 not in visited:
                    heapq.heappush(heap,(max(w1,w2),n2))
        return -1

        