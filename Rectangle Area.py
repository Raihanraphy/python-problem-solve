class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = self.getRectangleArea(ax1, ay1, ax2, ay2)
        area2 = self.getRectangleArea(bx1, by1, bx2, by2)
        result = area1 + area2

        # check for intersection

        if ax1 > bx2 or ax2 < bx1 or ay1 > by2 or ay2 < by1:
            return result
        
        # Find intersection co-ordinates
        if ax1 < bx1:
            # a is to the left of b
            x1 = bx1
            x2 = min(ax2, bx2)
        else:
            # b is to the left of a
            x1 = ax1
            x2 = min(ax2, bx2)

        if ay1 < by1:
            # a is below b
            y1 = by1
            y2 = min(ay2, by2)
        else:
            y1 = ay1
            y2 = min(ay2, by2)

        commonArea = self.getRectangleArea(x1, y1, x2, y2)

        return result - commonArea

    def getRectangleArea(self, ax1, ay1, ax2, ay2):
        return abs(ax1 - ax2) * abs(ay1 - ay2)
