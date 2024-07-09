class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapper = {}
        for num in nums:
            if num in mapper.keys():
                mapper[num] += 1
            else:
                mapper[num] = 1
        
        for key, value in mapper.items():
            if value == 1:
                return key
        
        return