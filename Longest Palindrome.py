class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict={}
        count=0
        for i in s:
            my_dict[i]=my_dict.get(i,0)+1
        for ch in my_dict.values():
            if ch%2==0:
                count+=ch
            else:
                count+=ch-1
        if count<len(s):
            count+=1
        return count            
