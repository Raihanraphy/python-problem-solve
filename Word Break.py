class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        max_length = defaultdict(int)
        min_end = sys.maxsize
        words = set()
        for word in wordDict:
            words.add(word)
            c = word[0]
            max_length[c] = max(max_length[c], len(word))
            if word[-1] == s[-1]:
                min_end = min(min_end, len(word))
        if min_end == sys.maxsize:
            return False
        i = 0
        j = 0
        memo = {}
        def search(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return True
            if len(s) - start < min_end:
                return False
            c = s[start]
            if c not in max_length:
                return False
            j = start + 1
            cur = c
            while True:
                if cur in words:
                    if search(j):
                        return True
                if j == len(s) or j - start >= max_length[c]:
                    memo[start] = False
                    return False
                cur += s[j]
                j += 1
        return search(0)
