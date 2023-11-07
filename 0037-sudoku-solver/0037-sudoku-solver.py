class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n = len(board)

        def solve(board):
            for row in range(n):
                for col in range(n):
                    if board[row][col] == ".":
                        for i in range(1, 10):
                            if isValid(row, col, board, n, str(i)):
                                board[row][col] = str(i)

                                if solve(board):
                                    return True
                                else:
                                    board[row][col] = "."
                        return False
            return True
        
        solve(board)


def isValid(row, col, board, n, charac):
    for i in range(n):
        if board[i][col] == charac:
            return False
        
        if board[row][i] == charac:
            return False
        
        if board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == charac:
            return False
        
    return True