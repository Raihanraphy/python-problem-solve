class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t == 0 and len(set(nums)) == len(nums):
            
            return False
            
        
        size = len(nums)
        
        bucket = {}
        
        width = t + 1
        
        for idx, number in enumerate(nums):
            
            bucket_idx = number // width
            
            if bucket_idx in bucket:
                return True
            
            elif bucket_idx + 1 in bucket and abs(number - bucket[bucket_idx + 1]) < width:
                return True
            
            elif bucket_idx - 1 in bucket and abs(number - bucket[bucket_idx - 1]) < width:
                return True

            bucket[bucket_idx] = number
            if idx >= k:
                del bucket[ nums[idx-k] //width ]
                
        return False
