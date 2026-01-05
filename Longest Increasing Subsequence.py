import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # lis_ending_with[i] is the lowest number ending a SIS of length i + 1 (so far)
        lis_ending_with = [nums[0]]

        for end in range(1, len(nums)):
            idx = bisect_left(lis_ending_with, nums[end])
            if idx == len(lis_ending_with):
                lis_ending_with.append(nums[end])
            else:
                lis_ending_with[idx] = min(lis_ending_with[idx], nums[end])

        return len(lis_ending_with)
