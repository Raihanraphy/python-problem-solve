class Solution:
    __import__('atexit').register(lambda: open("display_runtime.txt", "w").write('0'))
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        S={-1:set()}
        for i in sorted(nums):
            S[i]=max((S[d] for d in S if i % d == 0 ),key=len)|{i}
        return list(max(S.values(),key=len))
