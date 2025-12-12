class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        occurance = len(nums) // 3
        answer = []
        counter = {}
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1

        for k, v in counter.items():
            if v > occurance:
                answer.append(k)
        
        return answer

       
        
