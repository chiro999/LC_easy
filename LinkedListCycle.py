# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Check if the linked list is empty
        if not head:
            return False
        
        # Initialize two pointers, slow and fast, to the head of the linked list
        slow = fast = head
        
        # Infinite loop to traverse the linked list
        while True:
            # Move the slow pointer one step at a time
            slow = slow.next
            
            # Check if the fast pointer and its next node are not None
            if fast.next:
                # Move the fast pointer two steps at a time
                fast = fast.next.next
            else:
                # If the fast pointer or its next node is None, there is no cycle
                return False
            
            # Check if either the fast or slow pointer becomes None during the traversal
            if not fast or not slow:
                return False
            
            # Check if the fast and slow pointers meet, indicating a cycle
            if fast == slow:
                return True
