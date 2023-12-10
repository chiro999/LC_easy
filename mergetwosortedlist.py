# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify the code
        dummy = cursor = ListNode(0)
        
        # Iterate while both linked lists have nodes
        while l1 and l2:
            # Compare the values of the current nodes in l1 and l2
            if l1.val < l2.val:
                # If l1's value is smaller, append l1 to the result
                cursor.next = l1
                l1 = l1.next
            else:
                # If l2's value is smaller or equal, append l2 to the result
                cursor.next = l2
                l2 = l2.next
            
            # Move the cursor to the last node in the result
            cursor = cursor.next

        # If one of the linked lists is exhausted, append the remaining one
        if l1 is None or l2 is None:
            cursor.next = l1 or l2

        # Return the merged linked list (excluding the dummy node)
        return dummy.next
