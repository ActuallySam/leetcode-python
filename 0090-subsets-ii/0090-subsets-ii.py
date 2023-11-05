class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ans = []

        def findSubsets(index, ds):
            ans.append(list(ds))
            for i in range(index, n):
                if index != i and nums[i] == nums[i - 1]:
                    continue
                
                ds.append(nums[i])
                findSubsets(i + 1, ds)
                ds.pop()
    
        nums.sort()
        findSubsets(0, [])
        return ans