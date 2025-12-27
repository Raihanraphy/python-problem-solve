# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.next_val = None
        self.iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.next_val is not None:
            return self.next_val
        elif self.iterator.hasNext():
            self.next_val = self.iterator.next()
            return self.next_val
        else:
            return None
        
    def next(self):
        """
        :rtype: int
        """
        if not self.next_val:
            return self.iterator.next()
        next_val = self.next_val
        self.next_val = None
        return next_val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.next_val is not None or self.iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

# 1,2,3
# None
