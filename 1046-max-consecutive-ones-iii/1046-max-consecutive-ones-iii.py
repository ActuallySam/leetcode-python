class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        l, r = 0, 0
        max_len, count_zeros = 0, 0

        for i in range(n):
            if nums[r] == 0:
                count_zeros += 1
            while count_zeros > k:
                if nums[l] == 0:
                    count_zeros -= 1
                l += 1
            if count_zeros <= k:
                max_len = max(max_len, r - l + 1)
            
            r += 1
        return max_len