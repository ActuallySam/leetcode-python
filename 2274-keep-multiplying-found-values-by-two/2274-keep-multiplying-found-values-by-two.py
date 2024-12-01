class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            if original in nums:
                original *= 2
        
        return original