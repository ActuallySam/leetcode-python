class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        n = len(sentence)
        m = len(searchWord)
        arr = []
        s = ""
        for i in range(n):
            if sentence[i] == " ":
                arr.append(s)
                s = ""
            else:
                s += sentence[i]
        if s:
            arr.append(s)
        
        minIndex = float('inf')
        for i in range(len(arr)):
            if len(arr[i]) < m:
                continue
            if arr[i].startswith(searchWord):
                minIndex = i + 1
                break

        return -1 if minIndex == float('inf') else minIndex