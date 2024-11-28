class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        n = len(nums)
        temp = []
        max_len = 1
        temp.append(nums[0])

        for i in range(n):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
                max_len += 1
            else:
                ind = bisect.bisect_left(temp, nums[i])
                temp[ind] = nums[i]
        
        return max_len