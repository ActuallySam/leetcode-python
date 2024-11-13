class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        n = len(nums)
        def atMostWithSum(goal):
            res = 0
            lo, hi = 0, n - 1     # two pointers to slide from head and tail of nums

            # fix the head
            while lo < hi:
                # keep sliding from hi if it violates the summation
                while lo < hi and nums[lo] + nums[hi] > goal:
                    hi -= 1

                # any sub-array within nums[lo: hi] and ending at hi
                # is guaranteed to have summ <= goal here
                # (nums[lo], nums[hi]), (nums[lo + 1], nums[hi]), ..., (nums[hi - 1], nums[hi])
                window = hi - lo
                res += window
            
                # move the header
                lo += 1
            
            return res

        n = len(nums)

        # 1. sort nums increasingly
        nums = sorted(nums)

        # 2. exact (lower <= sum <= upper) := atMostWithSum(sum = upper) - atMostWithSum(sum = lower - 1)
        return atMostWithSum(upper) - atMostWithSum(lower - 1)