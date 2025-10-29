class Solution:
    def trailingZeroes(self, n: int) -> int:
        div=5
        res=0
        quo=0
        while(n>=div):
            quo=n//div
            res=res+quo
            div=div*5
        return (res)
