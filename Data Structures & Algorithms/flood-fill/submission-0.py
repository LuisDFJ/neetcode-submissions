class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        N,M = len(image),len(image[0])
        visit = set()
        def dfs(r: int, c:int, col: int):
            nonlocal image, color, visit
            if r < 0 or c < 0 or r >= N or c >= M or image[r][c] != col or (r,c) in visit:
                return
            image[r][c] = color
            visit.add((r,c))
            for n,m in [ (r-1,c), (r+1,c), (r,c-1), (r,c+1) ]:
                dfs(n,m,col)
        dfs(sr,sc,image[sr][sc])
        return image
