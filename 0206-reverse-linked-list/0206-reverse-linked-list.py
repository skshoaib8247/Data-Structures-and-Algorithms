class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        i=0
        hs={}
        while temp!=None:
            hs[i]=temp.val
            temp=temp.next
            i+=1
        temp=head
        for i in range(len(hs)-1,-1,-1):
            temp.val=hs[i]
            temp=temp.next
        return head

#  while temp.next!=None:  STOPS
# 4.next = None