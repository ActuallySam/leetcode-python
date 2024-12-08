class Solution(object):
    def constructTransformedArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [None] * n

        for i in range(n):
            if nums[i] == 0:
                res[i] = nums[i]
            else:
                pos = (i + (nums[i] % n) + n) % n
                res[i] = nums[pos]
        
        return res