from xarray.util.generate_aggregations import TEMPLATE_RETURNS


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1




    def print_list(self):
        temp = self.head
        print("The linked list is:")
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length ==0:
            self.head = None
            self.tail = None
        return temp.value

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value

    def get (self, index):
        if index <0 or index > self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set (self, index, value):
        if index <0 or index > self.length:
            return False
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert ( self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range (self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after




my_linked_list = LinkedList(4)
my_linked_list.append(3)
my_linked_list.append(7)
my_linked_list.prepend(6)
my_linked_list.prepend(9)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.set( 1, 2)
my_linked_list.print_list()
my_linked_list.insert(2,10)
my_linked_list.print_list()
my_linked_list.reverse()
my_linked_list.print_list()

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)