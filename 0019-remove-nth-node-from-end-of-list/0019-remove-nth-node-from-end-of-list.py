# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       i=0
       length=0
       temp=head
       while temp:
         temp=temp.next
         length+=1
       if length==n:
           newhead=head.next
           return newhead
       pos_to_remove=length-n
       count=1
       temp=head
       while count<pos_to_remove:
           count+=1
           temp=temp.next
       temp.next=temp.next.next
       return head


       
    