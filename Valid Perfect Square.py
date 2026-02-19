class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<2:
            return True
        left = 2
        right = (num//2)+1
        while(left<=right):
            mid = (left+right)//2
            sq = mid*mid
            if sq==num:
                return True
            elif sq>num:
                right = mid-1
            else:
                left = mid+1
        return False

        
