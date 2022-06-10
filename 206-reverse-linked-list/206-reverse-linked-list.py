# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        current=head
        prev=None
        while current != None:
            next=current.next
            current.next=prev
            prev=current
            current=next
        return prev
        
        