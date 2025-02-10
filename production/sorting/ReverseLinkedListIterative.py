class ListNode:
    def __inti__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList (self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next_node = curr.next  # Store next node
            curr.next = prev  # Reverse link
            prev = curr  # Move prev ahead
            curr = next_node  # Move curr ahead
        return prev  # New head

    # Example usage:
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print("Original List:")
print_list(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
print_list(reversed_head)