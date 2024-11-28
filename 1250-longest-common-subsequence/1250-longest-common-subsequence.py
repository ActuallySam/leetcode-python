class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n, m = len(text1), len(text2)
        prev = [0 for _ in range(m + 1)]
        curr = [0 for _ in range(m + 1)]

        for j in range(m):
            prev[j] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i -1] == text2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
                else:
                    curr[j] = max(prev[j], curr[j - 1])
            prev = curr[:]

        return prev[m]