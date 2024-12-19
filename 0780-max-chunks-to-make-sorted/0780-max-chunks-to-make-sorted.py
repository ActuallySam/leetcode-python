class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        running_sum, expected_sum, chunks = 0, 0, 0
        for i in range(len(arr)):
            running_sum += arr[i]
            expected_sum += i
            if running_sum == expected_sum:
                chunks += 1
        return chunks