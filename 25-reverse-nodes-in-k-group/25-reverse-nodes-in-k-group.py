# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        dummy_node=ListNode(0,head)
        group_prev=dummy_node
        nextK=self.getKth(group_prev,k)
        last= group_prev.next
        # first=self.reverseKNodes(head,k)
        # return last
    
        while nextK!=None:
            next=nextK.next
            self.reverseKNodes(group_prev.next, k)
            #nextK=head
            group_prev.next=nextK
            last.next=next
            group_prev=last
            nextK=self.getKth(group_prev,k)
            last= group_prev.next
        return dummy_node.next
        
            
    def getKth(self, curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
    
    def reverseKNodes(self, first, k):
        current=first
        left_node_prev=None
        prev=None
        left_node=current
        for i in range(k):
            next=current.next
            current.next=prev
            prev=current
            current=next
        first=prev
        left_node.next=current
        
        