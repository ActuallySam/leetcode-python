class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        # Find the smallest value in array and perform ops on that
        res = nums[:]
        while k:
            smallest = sorted(res)[0]
            smallest_ele_index = res.index(smallest)
            res[smallest_ele_index] *= multiplier
            k -= 1
        return res