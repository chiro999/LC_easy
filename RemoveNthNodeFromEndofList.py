# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Initialize slow and fast pointers to the head of the linked list.
        slow = head
        fast = head

        # Move the fast pointer n steps ahead to create a gap of n nodes.
        for i in range(n):
            fast = fast.next

        # If fast pointer reaches the end, it means the Nth node is the head.
        if not fast:
            return head.next

        # Iterate both pointers until the fast pointer reaches the end.
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Adjust the next pointer of the slow node to skip the Nth node.
        slow.next = slow.next.next

        # Return the head of the modified linked list.
        return head
