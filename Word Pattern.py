class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        dic_c = {}
        dic_word = {}
        if len(pattern) != len(words): return False
        for c, word in zip(pattern, words):
            if not c in dic_c and not word in dic_word:
                dic_c[c] = word
                dic_word[word] = c
            elif (c in dic_c and dic_c[c] != word) or (word in dic_word and dic_word[word] != c):
                return False
        return True
