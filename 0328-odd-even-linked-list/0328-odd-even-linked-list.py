# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        astack=[]
        bstack=[]
        temp=head
        i=1
        while temp:
            if (i)%2==0:
               astack.append(temp.val)
            else:
                bstack.append(temp.val)
            temp=temp.next
            i+=1
        temp=head
        for i in range(len(bstack)):
            temp.val=bstack[i]
            temp=temp.next
        for i in range(len(astack)):
            temp.val=astack[i]
            temp=temp.next
        return head

            
               
