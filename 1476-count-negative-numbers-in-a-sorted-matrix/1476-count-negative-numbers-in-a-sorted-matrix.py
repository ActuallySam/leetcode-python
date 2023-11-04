class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_len = len(grid)
        count = 0
        for i in grid:
            for j in i:
                if j < 0:
                    count += 1
        
        return count