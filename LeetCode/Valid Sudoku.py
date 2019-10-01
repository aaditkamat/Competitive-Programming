# Title: Valid Sudoku
# Runtime: 100 ms
# Memory: 13.9 MB

class Solution:
    def checkNoRepetition(self, grid: List[str]) -> bool:
        values = set()
        for num in grid:
            if num != "." and num in values:
                return False
            values.add(num)
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i]
            if not self.checkNoRepetition(row):
                return False
        
        for j in range(9):
            column = []
            for i in range(9):
                column.append(board[i][j])
            if not self.checkNoRepetition(column):
                return False
            
        for x_left in range(0, 7, 3):
            for y_top in range(0, 7, 3):
                grid = [board[i][j] for i in range(x_left, x_left + 3) for j in range(y_top, y_top + 3)]
                if not self.checkNoRepetition(grid):
                    return False
            
        return True
        