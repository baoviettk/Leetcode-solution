# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
                    
        def reverseK(head):
            dummy=head
            cur,prev=head,None
            for i in range(k):
                next=cur.next
                cur.next=prev
                prev=cur
                cur=next
            return prev, head
        
        dummy=ListNode(0,head)
        prevTail= dummy
        cur=head
        while True:
            last=prevTail
            for i in range(k):
                if not last.next:
                    return dummy.next
                last=last.next
            nextHead=last.next
            f,l=reverseK(prevTail.next)
            prevTail.next=f
            l.next=nextHead
            prevTail=l
        
