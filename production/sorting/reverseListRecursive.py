class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head  # Base case: return the last node as the new head

        new_head = self.reverseList(head.next)  # Recursively reverse rest of the list
        head.next.next = head  # Reverse link
        head.next = None  # Break old link

        return new_head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print("Original List:")
print_list(head)

sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
print_list(reversed_head)