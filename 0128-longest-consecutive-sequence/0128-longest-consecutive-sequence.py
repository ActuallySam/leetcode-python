class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums = sorted(nums)
        max_count = 0
        sequence_length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    sequence_length += 1
                else:
                    max_count = max(max_count, sequence_length)
                    sequence_length = 1
        
        return max(max_count, sequence_length)
        