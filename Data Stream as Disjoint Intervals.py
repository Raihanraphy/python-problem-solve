from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        n = len(intervals)

        i = bisect_left(intervals, [value, value])

        # check left interval
        left_merge = (i > 0 and intervals[i-1][1] + 1 >= value)
        # check right interval
        right_merge = (i < n and intervals[i][0] - 1 <= value)

        if left_merge and right_merge:
            # merge both sides
            intervals[i-1][1] = intervals[i][1]
            intervals.pop(i)

        elif left_merge:
            # extend left interval
            intervals[i-1][1] = max(intervals[i-1][1], value)

        elif right_merge:
            # extend right interval (shift start)
            intervals[i][0] = min(intervals[i][0], value)

        else:
            # new interval
            intervals.insert(i, [value, value])

    def getIntervals(self):
        return self.intervals
