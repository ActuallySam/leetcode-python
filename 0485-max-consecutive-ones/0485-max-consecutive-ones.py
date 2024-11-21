class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 0
        count = 0
        l, r = 0, 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
                max_len = max(max_len, count)
                r += 1
            else:
                l = r
                count = 0
                continue
        return max_len