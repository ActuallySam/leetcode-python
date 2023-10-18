class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mapper1 = {}
        mapper2 = {}
        for ch in s:
            mapper1[ch] = mapper1.get(ch, 0) + 1
        for ch in t:
            mapper2[ch] = mapper2.get(ch, 0) + 1
        
        return mapper1 == mapper2
