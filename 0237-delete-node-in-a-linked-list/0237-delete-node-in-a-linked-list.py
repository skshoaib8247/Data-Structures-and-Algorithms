# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        Do not return anything, modify node in-place instead.
        """
        # Copy the value from the next node
        node.val = node.next.val
        # Skip the next node
        node.next = node.next.next
