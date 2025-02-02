class Node:
    """Node class for the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    """Queue implementation using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        """Add an element to the rear of the queue."""
        new_node = Node(value)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove an element from the front of the queue."""
        if self.front is None:  # If the queue is empty
            print("Queue is empty")
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty
            self.rear = None
        self.size -= 1
        return value

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def peek(self):
        """Return the front element without removing it."""
        if self.front is None:
            return None
        return self.front.value

    def __len__(self):
        """Return the size of the queue."""
        return self.size

# Example usage
if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Dequeued:", q.dequeue())  # Output: 10
    print("Front element:", q.peek())  # Output: 20
    print("Queue size:", len(q))  # Output: 2