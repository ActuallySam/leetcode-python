class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0]:
            return 0
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[0][0] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] or (i == 0 and j == 0):
                    continue
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[ROWS-1][COLS-1]