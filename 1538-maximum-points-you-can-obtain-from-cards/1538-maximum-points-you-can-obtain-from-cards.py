class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n = len(cardPoints)
        max_score = 0
        lsum, rsum = 0, 0
        l, r = 0, n - 1

        for i in range(k):
            lsum = lsum + cardPoints[i]
            max_score = lsum

        for i in range(k-1, -1, -1):
            lsum -= cardPoints[i]
            rsum += cardPoints[r]
            r -= 1
            max_score = max(max_score, lsum + rsum)
        
        return max_score

