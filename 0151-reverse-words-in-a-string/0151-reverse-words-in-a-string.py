class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word_list = s.split()
        revered_string = word_list[::-1]
        return " ".join(revered_string)
        