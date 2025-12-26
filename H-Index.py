class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_idx = len(citations)
        citations.sort()

        for i, citation in enumerate(citations):
            if citation >= h_idx:
                return h_idx
            h_idx -= 1

        return 0
