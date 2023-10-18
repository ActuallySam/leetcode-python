class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Map
        # mapper = {}
        # for num in nums:
        #     if not mapper.get(num):
        #         mapper[num] = 1
        #     else:
        #         mapper[num] += 1
        
        # for val in mapper:
        #     if mapper[val] > 1:
        #         return True
        
        # return False

        # Set
        numset = set()
        for num in nums:
            if num in numset:
                return True
            else:
                numset.add(num)
        
        return False
