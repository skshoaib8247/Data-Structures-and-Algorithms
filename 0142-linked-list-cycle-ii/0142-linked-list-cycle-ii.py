# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=0
        hash_set={}
        temp=head
        while temp:
            if temp in hash_set:
                return temp
            hash_set[temp]=i
            temp=temp.next
            i+=1
        return None
