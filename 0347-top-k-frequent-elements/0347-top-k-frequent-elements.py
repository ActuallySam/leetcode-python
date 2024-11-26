import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        n = len(nums)
        mapper = dict(Counter(nums))
        heap = []

        for key, value in mapper.items():
            heapq.heappush(heap, [value, key])
            if len(heap) > k:
                heapq.heappop(heap)
        
        while len(heap) > 0:
            element = heapq.heappop(heap)
            res.append(element[1])
        
        return res