class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        dif = x - y
        dif2 = y - x 
        derivdif = x - (y - (x - y))
        derivdif2 = y - (x - (y - x))
        mod1 = x % y
        mod2 = y % x
        inc1 = y - mod1
        inc2 = x - mod2
        if x + y < target: return False
        if mod1 and mod2:
            return x == target or y == target or target == 0 or dif == target or dif2 == target or derivdif == target or derivdif2 == target or x + y == target or derivdif2 + x == target or derivdif + y == target or target % inc1 == 0 or target % inc2 == 0 or x % mod1 == target % mod1 or y % mod2 == target % mod2
        
        else:
            return x == target or y == target or target == 0 or dif == target or dif2 == target or derivdif == target or derivdif2 == target or x + y == target or derivdif2 + x == target or derivdif + y == target or target % inc1 == 0 or target % inc2 == 0 
        
