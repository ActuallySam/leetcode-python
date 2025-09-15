class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = 0
        word_list = text.split(" ")
        n = len(word_list)
        for word in word_list:
            for brokenLetter in brokenLetters:
                if brokenLetter in word:
                    words += 1
                    break
        return n - words