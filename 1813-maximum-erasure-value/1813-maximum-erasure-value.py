class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        n = len(nums)
        vis = set()
        left = 0
        curr_sum = 0
        for right in range(n):
            while nums[right] in vis:
                curr_sum -= nums[left]
                vis.remove(nums[left])
                left += 1

            curr_sum += nums[right]
            vis.add(nums[right])
            max_score = max(max_score, sum(vis))
        return max_score
        