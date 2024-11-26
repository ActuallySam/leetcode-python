class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MASK = 0xFFFFFFFF
        while b & MASK != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        
        return a & MASK if b > MASK else a