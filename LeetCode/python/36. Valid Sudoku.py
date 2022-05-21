#Appraoch 1:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashSet = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in hashSet:
                    return False
                else:
                    hashSet.add(board[i][j])
            hashSet.clear()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in hashSet:
                    return False
                else:
                    hashSet.add(board[j][i])
            hashSet.clear()
        
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and (i//3, board[j][i], j//3) in hashSet:
                    return False
                else:
                    hashSet.add((i//3, board[j][i], j//3))
        
        return True


# Approach 2:
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        sudoku = []
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != '.':
                    sudoku.append((col, i))
                    sudoku.append((j, col))
                    sudoku.append((i//3, col, j//3))
        
        return len(sudoku) == len(set(sudoku))
