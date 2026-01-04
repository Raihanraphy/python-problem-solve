class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        self.helper(s, 0, 0, ["(", ")"], res)
        return res
    def helper(self, s, last_i, last_j, pairs, res):
        count = 0
        for i in range(last_i, len(s)):
            if s[i] == pairs[0]:
                count += 1
            elif s[i] == pairs[1]:
                count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if s[j] == pairs[1] and (j == last_j or s[j - 1] != pairs[1]):
                    self.helper(s[0:j] + s[j+1:], i, j, pairs, res)
            return
        s = s[::-1]
        if pairs[0] == "(":
            self.helper(s, 0, 0, [")", "("], res)
        else:
            res.append(s)
