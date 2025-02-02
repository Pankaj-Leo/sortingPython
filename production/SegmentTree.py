class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.seg_tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    # Build segment tree
    def build(self, arr, index, left, right):
        if left == right:  # Leaf node
            self.seg_tree[index] = arr[left]
            return

        mid = (left + right) // 2
        self.build(arr, 2 * index + 1, left, mid)
        self.build(arr, 2 * index + 2, mid + 1, right)

        self.seg_tree[index] = self.seg_tree[2 * index + 1] + self.seg_tree[2 * index + 2]  # Sum

    # Query sum in range [ql, qr]
    def query(self, ql, qr):
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, index, left, right, ql, qr):
        if ql <= left and qr >= right:  # Total overlap
            return self.seg_tree[index]
        if ql > right or qr < left:  # No overlap
            return 0

        mid = (left + right) // 2
        return self._query(2 * index + 1, left, mid, ql, qr) + \
               self._query(2 * index + 2, mid + 1, right, ql, qr)

    # Update an element at position pos
    def update(self, pos, new_val):
        self._update(0, 0, self.n - 1, pos, new_val)

    def _update(self, index, left, right, pos, new_val):
        if left == right:
            self.seg_tree[index] = new_val
            return

        mid = (left + right) // 2
        if pos <= mid:
            self._update(2 * index + 1, left, mid, pos, new_val)
        else:
            self._update(2 * index + 2, mid + 1, right, pos, new_val)

        self.seg_tree[index] = self.seg_tree[2 * index + 1] + self.seg_tree[2 * index + 2]  # Sum update

# Example Usage
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print("Sum of range [1,4]:", st.query(1, 4))
st.update(2, 10)  # Update arr[2] = 10
print("Sum of range [1,4] after update:", st.query(1, 4))