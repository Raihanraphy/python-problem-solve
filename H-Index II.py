class Solution:
    def hIndex(self, citations):
        n = len(citations)
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2

                return n - mid

            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid - 1

        return n - left
