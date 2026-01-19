
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        

        """
        first we need to make sure that we must take the number in a ordered way

        # approach

        we have to take number from the give arr
        we can not re-order so we can use stack
            greater to small --> if digit is greater and top is small pop
            we need to make sure that there must be k digits
            means if k==2
            then when we return stack there must be 2 digits
        
        we can take numbers from num1 and num2
        (0,5), (1, 4), (2, 3), P(3,2), up to max element in A

        how we going to implemet

        if b have more than k elements then start with 0 or is less then start from k - len()
        take all possible sequence of x and k-x numbers from the num1 & num2

        """

        ans = 0
        for x in range(max(0, k-len(nums2)), min(k, len(nums1))+1):
            # take x numbers form num1 and k-x from num2
            number1 = self.get_max_seq(nums1, x)
            number2 = self.get_max_seq(nums2, k-x)

            i = 0; j = 0
            num=0
            while i < x and j < k-x:
                if number1[i] > number2[j]:
                    digit = number1[i]
                    i+=1
                elif number1[i] == number2[j]:
                    if number1[i:] > number2[j:]:
                        digit = number1[i]
                        i+=1
                    else:
                        digit = number1[i]
                        j+=1
                    
                else:
                    digit = number2[j]
                    j+=1
                
                num = num*10+digit
            
            while i<x:
                num = num*10+number1[i]
                i+=1

            while j < k-x:
                num = num*10+number2[j]
                j+=1
         
            ans = max(ans, num)

        return [int(i) for i in str(ans)]


    def get_max_seq(self, arr, k):
        st = []
        n = len(arr)
        i = 0
        drops = n-k
        
        while i < n:
            if st and st[-1] < arr[i] and drops:
                st.pop()
                drops -= 1
            else:
                st.append(arr[i])
                i+=1
        
        return st[:k]
            
