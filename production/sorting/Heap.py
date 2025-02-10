class MinHeap:
    def __init__(self, arr=None):
        self.heap = []
        if isinstance(arr, list):
            self.heap = arr[:]
            for i in range(len(self.heap) // 2, -1, -1):
                self._sift_down(i)

    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        size = len(self.heap)
        while True:
            left, right, smallest = 2 * i + 1, 2 * i + 2, i
            if left < size and self.heap[left] < self.heap[smallest]: smallest = left
            if right < size and self.heap[right] < self.heap[smallest]: smallest = right
            if smallest == i: break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def insert(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap: return None
        if len(self.heap) == 1: return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def update(self, index, new_val):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        old_val = self.heap[index]
        self.heap[index] = new_val
        if new_val < old_val: self._sift_up(index)
        else: self._sift_down(index)

    def delete(self, index):
        if index < 0 or index >= len(self.heap):
            raise IndexError("Index out of range")
        self.update(index, float('-inf'))
        self.extract_min()

    def get_min(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def print_heap(self):
        print(self.heap)


class MaxHeap(MinHeap):
    def _sift_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        size = len(self.heap)
        while True:
            left, right, largest = 2 * i + 1, 2 * i + 2, i
            if left < size and self.heap[left] > self.heap[largest]: largest = left
            if right < size and self.heap[right] > self.heap[largest]: largest = right
            if largest == i: break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest

    def extract_max(self):
        return self.extract_min()  # Inherited method, but acts as extract_max due to sift logic

    def get_max(self):
        return self.get_min()  # MinHeap's get_min() now returns max due to overridden sift functions


# Example Usage
arr = [3, 9, 2, 1, 4, 5]

print("MinHeap Operations:")
min_heap = MinHeap(arr)
min_heap.print_heap()
min_heap.insert(0)
min_heap.print_heap()
print("Extracted Min:", min_heap.extract_min())
min_heap.print_heap()
min_heap.delete(2)
min_heap.print_heap()

print("\nMaxHeap Operations:")
max_heap = MaxHeap(arr)
max_heap.print_heap()
max_heap.insert(10)
max_heap.print_heap()
print("Extracted Max:", max_heap.extract_max())
max_heap.print_heap()
max_heap.delete(2)
max_heap.print_heap()
