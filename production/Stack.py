class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        """Constructor to initialize the stack"""
        self.top = None
        self.size = 0

    def push(self, value):
        """Push a value onto the stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Pop a value off the stack"""
        if self.is_empty():
            return "Stack is empty!"
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None

    def peek(self):
        """Peek the top value of the stack without removing it"""
        if not self.is_empty():
            return self.top.value
        else:
            return "Stack is empty!"

    def __str__(self):
        """String representation of the stack"""
        result = []
        current = self.top
        while current:
            result.append(current.value)
            current = current.next
        return "Stack: " + " -> ".join(map(str, result))


# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print(stack)  # Stack: 30 -> 20 -> 10
    print(stack.pop())  # 30
    print(stack)  # Stack: 20 -> 10
    print(stack.peek())  # 20