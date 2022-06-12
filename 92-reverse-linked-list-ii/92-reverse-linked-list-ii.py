# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        current=head
        left_node_prev=None
        for i in range(left-1):
            left_node_prev=current
            current=current.next
        prev=None
        left_node=current
        for i in range(left,right+1):
            next=current.next
            current.next=prev
            prev=current
            current=next
        if left_node_prev != None:
            left_node_prev.next=prev
        else:
            head=prev
        left_node.next=current
        
        return head
        
        
            
            