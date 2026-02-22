class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        exp=0
        for e in b:
            exp=e+10*exp
            exp%=1140
        if exp==0: exp=1140 #Add this line can save old solution
        return pow(a, exp, 1337)
        
