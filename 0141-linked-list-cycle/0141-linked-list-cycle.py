# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        hash_set={}
        i=0
        temp=head
        while temp:
            if temp in hash_set:
                return True
            hash_set[temp]=i
            temp=temp.next
            i+=1
        return False