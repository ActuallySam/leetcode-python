class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """        
        if (n & n-1) == 0 and (n-1) % 3 == 0:
            return True
        
        return False
        
        