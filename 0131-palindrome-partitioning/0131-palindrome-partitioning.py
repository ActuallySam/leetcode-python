class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        ans = []
        n = len(s)

        def recursion(s, index, ds):
            if index == n:
                ans.append(ds[:])
                return

            for i in range(index, n):
                if isPalindrome(s, index, i):
                    ds.append(s[index:i+1])
                    recursion(s, i + 1, ds)
                    ds.pop()
        
        recursion(s, 0, [])
        return ans

def isPalindrome(string, start, end):
    while start <= end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True