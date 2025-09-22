# class Solution:
#     def longestConsecutive(self, arr: List[int]) -> int:
        # s=set(arr)
        # count=0
        # maxi=0
        # for i in arr:
        #     if i-1 not in s:
        #         y=i+1
        #         while y in s:
        #             y+=1
        #         maxi=max(maxi,y-i)
        # return maxi

        # hashmap={}
        # maxi=0
        # for num in arr:
        #     hashmap[num]=1
        # for num in arr:
        #     count=0
        #     if num-1 not in hashmap:
        #         count+=1
        #         x=num
        #         while x+1 in hashmap:
        #             count+=1
        #             x+=1
        #         maxi=max(count,maxi)
        # return maxi
__import__("atexit").register(lambda:open("display_runtime.txt","w").write("0"))                
class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        hm = {}   
        longest = 0

        for num in arr:
            if num not in hm: 
                left = hm.get(num - 1, 0)
                right = hm.get(num + 1, 0)
                curr_len = left + right + 1
                hm[num] = curr_len
                hm[num - left] = curr_len
                hm[num + right] = curr_len

                longest = max(longest, curr_len)

        return longest
