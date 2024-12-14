class Solution(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_deque, min_deque = deque(), deque()
        l, ans = 0, 0

        for r in range(n):
            while max_deque and nums[r] > max_deque[-1]: max_deque.pop()
            while min_deque and nums[r] < min_deque[-1]: min_deque.pop()

            max_deque.append(nums[r])
            min_deque.append(nums[r])

            while max_deque[0] - min_deque[0] > 2:
                if nums[l] == max_deque[0]: max_deque.popleft()
                if nums[l] == min_deque[0]: min_deque.popleft()
                l += 1

            ans += r - l + 1
        return ans
