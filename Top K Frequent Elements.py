class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        max_freq = max(counts.values())
        bucket = [[] for _ in range(max_freq + 1)]
        for key, value in counts.items():
            bucket[value].append(key)

        return [item for sublist in bucket for item in sublist][-k:]
