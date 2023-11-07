class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(dist)
        arrival_time = [0] * n

        for i in range(n):
            arrival_time[i] = (dist[i] - 1) / speed[i]
        
        arrival_time.sort()

        for i in range(n):
            if i > arrival_time[i]:
                return i
        
        return n