class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        cells = defaultdict(set)

        for row in range(9):
            for col in range(9):
                v = board[row][col]
                if v == ".": continue
                cell = row // 3, col // 3
                if v in rows[row] or v in cols[col] or v in cells[cell]:
                    return False
                rows[row].add(v)
                cols[col].add(v)
                cells[cell].add(v)
        return True

