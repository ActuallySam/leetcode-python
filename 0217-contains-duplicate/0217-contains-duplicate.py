class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        unique_set = set()
        for num in nums:
            if num in unique_set:
                return True
            unique_set.add(num)
        return False