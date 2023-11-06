class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ans = []
        board = [None] * n
        s = "." * n
        for i in range(n):
            board[i] = s

        def solve(col, board, ans):
            if col == n:
                ans.append(list(board))
                return

            for row in range(n):
                if isSafe(row, col, board, n):
                    board[row] = board[row][:col] + "Q" + board[row][col + 1:]
                    solve(col + 1, board, ans)
                    board[row] = board[row][:col] + "." + board[row][col + 1:]
        
        solve(0, board, ans)
        return ans

def isSafe(row, col, board, n):
    duprow = row
    dupcol = col

    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1
    
    row = duprow
    col = dupcol

    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1
    
    row = duprow
    col = dupcol

    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True
    