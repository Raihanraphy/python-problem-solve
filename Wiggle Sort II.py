class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        m = len(nums)
        large_index = m - 1
        small_index = (m - 1) // 2
        # if odd, put the large half
        # if even, put the small half
        for i in range(m):
            if i % 2 == 1:
                nums[i] = sorted_nums[large_index]
                large_index -= 1
            else:
                nums[i] = sorted_nums[small_index]
                small_index -= 1
    #[1,1,1,1,2,2,2]
    #[1,1,1,2,2,2,2] -> no
    #[1,1,1,2,2,2] -> [1,2,1,2,1,2]
    # 7 -> 3, 6->2
