class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapper = {}
        for x, num in enumerate(nums):
            y = target - num
            if y in mapper.keys():
                return [mapper[y], x]
            mapper[num] = x

        return []