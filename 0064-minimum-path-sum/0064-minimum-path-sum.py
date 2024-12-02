class Solution(object):
    def rec(self, r, c, grid, dp):
        if r < 0 or c < 0:
            return float('inf')
        
        
        if dp[r][c] != -1:
            return dp[r][c]

        return 

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 and c == 0:
                    dp[r][c] = grid[0][0]
                elif r == 0:
                    dp[r][c] = dp[r][c-1] + grid[r][c]
                elif c == 0:
                    dp[r][c] = dp[r-1][c] + grid[r][c]
                else:
                    dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])

        return dp[ROWS-1][COLS-1]