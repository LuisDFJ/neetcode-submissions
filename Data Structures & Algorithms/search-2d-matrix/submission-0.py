class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        idx = lambda i: (i//cols,i%cols)

        left,right = 0, rows*cols-1
        while left <= right:
            mid = (right+left)//2
            i,j = idx(mid)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        