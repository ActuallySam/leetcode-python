class Solution:
    def maximumScore(self, nums, k):
        i = k
        j = k
        maxi = float('-inf')
        n = len(nums)
        mini = nums[k]
        while i >= 0 and j < n:
            maxi = max(maxi, mini * (j - i + 1))
            if j + 1 < n and i - 1 >= 0:
                if nums[j + 1] > nums[i - 1]:
                    j += 1
                    mini = min(mini, nums[j])
                else:
                    i -= 1
                    mini = min(mini, nums[i])
            elif j + 1 >= n:
                i -= 1
                if i >= 0:
                    mini = min(mini, nums[i])
            elif i - 1 < 0:
                j += 1
                if j < n:
                    mini = min(mini, nums[j])
        return maxi