class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []

        def findSubsets(index, ds):
            if index >= n:
                ans.append(list(ds))
                return
            
            ds.append(nums[index])
            findSubsets(index + 1, ds)
            ds.pop()
            findSubsets(index + 1, ds)
    
        findSubsets(0, [])
        return ans