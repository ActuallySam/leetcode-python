class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        n = len(nums)
        vis = set()
        left = 0
        right = 0
        curr_sum = 0
        while right < n:
            if nums[right] in vis:
                max_score = max(max_score, sum(vis))
                while nums[right] in vis:
                    curr_sum -= nums[left]
                    vis.remove(nums[left])
                    left += 1

            curr_sum += nums[right]
            vis.add(nums[right])
            right += 1
            
        return max(max_score, sum(vis))
        