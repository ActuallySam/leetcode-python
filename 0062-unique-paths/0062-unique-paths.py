class Solution(object):
    def rec(self, r, c, dp, ROWS, COLS):
        if r == ROWS - 1 or c == COLS - 1:
            return 1
        
        if dp[r][c] != -1:
            return dp[r][c]

        dp[r][c] = self.rec(r + 1, c, dp, ROWS, COLS) + self.rec(r, c + 1, dp, ROWS, COLS)
        return dp[r][c]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # dp = [[1 for _ in range(n)] for _ in range(m)]
        # return self.rec(0, 0, dp, m, n)
        dp = [1] * n

        for r in range(1, m):
            for c in range(1, n):
                dp[c] = dp[c] + dp[c - 1]

        return dp[n-1]