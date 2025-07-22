class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        n = len(nums)
        vis = set()
        left = 0
        right = 0
        curr_sum = 0
        while right < n:
            num_right = nums[right]
            if num_right in vis:
                max_score = max(max_score, curr_sum)
                while num_right in vis:
                    num_left = nums[left]
                    curr_sum -= num_left
                    vis.remove(num_left)
                    left += 1

            curr_sum += num_right
            vis.add(num_right)
            right += 1
            
        return max(max_score, curr_sum)