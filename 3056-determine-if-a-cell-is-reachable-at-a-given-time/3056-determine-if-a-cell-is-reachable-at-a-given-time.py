class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        """
        :type sx: int
        :type sy: int
        :type fx: int
        :type fy: int
        :type t: int
        :rtype: bool
        """
        if t == 1 and sx == fx and sy == fy:
            return False
        return max((abs(sx - fx)), (abs(sy - fy))) <= t