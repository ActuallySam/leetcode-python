class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num in mapper.keys():
                return True
            else:
                mapper[num] = 1
        return False