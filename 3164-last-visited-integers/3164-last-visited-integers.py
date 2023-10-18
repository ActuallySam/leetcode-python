class Solution(object):
    def lastVisitedIntegers(self, words):
        """
        :type words: List[str]
        :rtype: List[int]
        """
        stack = []
        res = []
        total_visited_integers = 0
        consecutive_prevs = 0
        for word in words:
            if word != "prev":
                consecutive_prevs = 0
                total_visited_integers += 1
                stack.append(int(word))
            else:
                consecutive_prevs += 1
                if consecutive_prevs > total_visited_integers:
                    res.append(-1)
                else:
                    res.append(stack[-consecutive_prevs])
                    
        return res