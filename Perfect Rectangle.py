class Solution :
    def isRectangleCover( self, rectangles : List[List[int]] ) -> bool :
        container = set()
        sumArea = 0
        for rectangle in rectangles :
            x1 = rectangle[0]
            y1 = rectangle[1]
            x2 = rectangle[2]
            y2 = rectangle[3]
            sumArea += (x2 - x1) * (y2 - y1)
            container ^= { (x1, y1), (x1, y2), (x2, y1), (x2, y2) }
        if len(container) != 4:
            return False
        dl = min(container, key = lambda p : p[0] + p[1])
        ur = max(container, key = lambda p : p[0] + p[1])
        return sumArea == (ur[0] - dl[0]) * (ur[1] - dl[1])
