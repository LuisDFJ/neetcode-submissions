from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dRows = defaultdict(set)
        dCols = defaultdict(set)
        dBlocks = defaultdict(set)

        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                if cell == ".":
                    continue
                blockId = (i//3,j//3)
                if cell in dRows[i] or cell in dCols[j] or cell in dBlocks[(blockId)]:
                    return False
                dRows[i].add(cell)
                dCols[j].add(cell)
                dBlocks[blockId].add(cell)
        return True
