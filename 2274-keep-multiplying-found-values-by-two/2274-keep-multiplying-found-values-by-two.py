class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        mapper={}
        for num in nums:
            mapper[num] = 1
        while original in mapper.keys():
            original *= 2
        return original