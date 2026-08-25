class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R,C = len(matrix),len(matrix[0])
        self.prefix = [[0] * (C+1) for _ in range(R+1)]
        for r in range(R):
            total = 0
            for c in range(C):
                total += matrix[r][c]
                self.prefix[r+1][c+1] = total + self.prefix[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        return self.prefix[row2][col2] + self.prefix[row1-1][col1-1] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)