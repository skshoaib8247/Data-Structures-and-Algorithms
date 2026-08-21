# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      slow=head
      fast= head
      while slow and fast:
        slow=slow.next
        fast=fast.next
      return slow

class Solution:
    def middleNode(self, head):
        count = 0
        temp = head

        # Count nodes
        while temp:
            count += 1
            temp = temp.next

        # Move to middle
        temp = head
        for i in range(count // 2):
            temp = temp.next

        return temp
