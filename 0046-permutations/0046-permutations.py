class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)

        def recursiveCall(ds, freq):
            if len(ds) == n:
                ans.append(list(ds))
                return
            
            for i in range(n):
                if not freq[i]:
                    freq[i] = True
                    ds.append(nums[i])
                    recursiveCall(ds, freq)
                    ds.pop()
                    freq[i] = False

        ans = []
        recursiveCall([], [None] * n)
        return ans