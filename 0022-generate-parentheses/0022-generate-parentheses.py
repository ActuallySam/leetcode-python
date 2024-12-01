class Solution(object):
    def rec(self, left, right, st, res):
        if right < left:
            return
        
        if not left and not right:
            res.append(st)
            return res
        
        if left:
            self.rec(left - 1, right, st + "(", res)
        if right:
            self.rec(left, right - 1, st + ")", res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []

        res = []
        self.rec(n, n, "", res)
        return res