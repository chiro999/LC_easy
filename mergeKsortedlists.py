# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Define a helper function to merge two lists
        def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = cursor = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    cursor.next = l1
                    l1 = l1.next
                else:
                    cursor.next = l2
                    l2 = l2.next
                cursor = cursor.next
            if (l1 == None) or (l2 == None):
                cursor.next = l1 or l2
            return dummy.next

        # Get the number of lists
        numLists = len(lists)

        # If there are no lists, return None
        if numLists < 1:
            return None

        # Initialize the interval for merging
        interval = 1

        # Perform a divide-and-conquer approach to merge lists
        while interval < numLists:
            for i in range(0, numLists - interval, interval * 2):
                # Merge two lists at a time
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        # The merged list is at the 0th index
        return lists[0]
