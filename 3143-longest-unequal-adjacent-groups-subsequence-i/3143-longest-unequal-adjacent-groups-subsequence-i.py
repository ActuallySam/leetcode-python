class Solution(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        a = -1
        res = []
        for i in range(n):
            if groups[i] != a:
                a = groups[i]
                res.append(words[i])
        
        return res