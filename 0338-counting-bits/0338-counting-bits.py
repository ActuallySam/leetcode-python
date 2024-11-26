class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        size = n + 1
        res = [0] * size

        for i in range(1, size):
            res[i] = res[i >> 1] + (i & 1)
        return res