class Solution:
    def addDigits(self, num: int) -> int:
        if num <10:
            return num
        else:
            while len(str(num))>1:
           
                sum = 0
                while num:
                    d = num%10
                    sum += d
                    num = num//10
                num = sum
                if len(str(num))== 1:
                    return sum
                    break
                



        
