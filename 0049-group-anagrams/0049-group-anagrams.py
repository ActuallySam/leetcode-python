class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """        
        strs_table = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))

            if sorted_str not in strs_table:
                strs_table[sorted_str] = []

            strs_table[sorted_str].append(st)
        
        return list(strs_table.values())