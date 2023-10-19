class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1, stack2 = [], []

        for ch in s:
            if ch != "#":
                stack1.append(ch)
            else:
                if len(stack1) > 0:
                    stack1.pop()
        for ch in t:
            if ch != "#":
                stack2.append(ch)
            else:
                if len(stack2) > 0:
                    stack2.pop()
        
        updated_s = "".join(stack1)
        updated_t = "".join(stack2)

        # return [updated_s, updated_t]
        return updated_s == updated_t