class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, suffix = 1, 1
        n = len(nums)
        res = [1]*n
        for i in range(n):
            res[i] *= prefix
            prefix *= nums[i]

        for i in range(n-1,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
