class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        right_mirrored_chars = s[::-1]
        word_list = right_mirrored_chars.split()
        reversed_string = word_list[::-1]
        return " ".join(reversed_string)