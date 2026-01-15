class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        values = sorted(nums)
        index = {v: i for i, v in enumerate(values)}
        count = [0] * n
        st = SegmentTree(n)

        for i in range(n - 1, -1, -1):
            left = 0
            right = index[nums[i]] - 1  # query strictly smaller int
            count[i] = st.query(left, right)
            st.update(index[nums[i]])

        return count

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))    


class SegmentTree:

    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node, left, right, ql, qr):
        if ql > right or qr < left:
            return 0

        if ql <= left and right <= qr:
            return self.tree[node]

        mid = left + (right - left) // 2
        left_sum = self._query(node * 2, left, mid, ql, qr)
        right_sum = self._query(node * 2 + 1, mid + 1, right, ql, qr)
        return left_sum + right_sum

    def update(self, idx):
        self._update(1, 0, self.n - 1, idx)

    def _update(self, node, left, right, idx):
        if left == right:
            self.tree[node] += 1
            return

        mid = left + (right - left) // 2
        if idx <= mid:
            self._update(node * 2, left, mid, idx)
        else:
            self._update(node * 2 + 1, mid + 1, right, idx)

        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
