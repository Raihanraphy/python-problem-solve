class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[False, []] for _ in range(len(s)+1) ]
        dp[len(s)] = [True,[""]] 

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <= len(s) and s[i:i+len(w)] == w: 
                    if dp[i+len(w)][0] == True:
                        new_sentence = [w + ("" if sentence == "" else " " + sentence) for sentence in dp[i + len(w)][1]]
                        dp[i][1].extend(new_sentence)
                        dp[i][0] = True 
        return dp[0][1]
