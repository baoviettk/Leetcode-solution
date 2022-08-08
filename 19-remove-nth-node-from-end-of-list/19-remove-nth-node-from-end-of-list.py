# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        length=0
        current=head
        
        while(current!=None):
            length+=1
            current=current.next
        if n>length:
            return head
        current=dummy
        for i in range(length-n):
            current=current.next
        current.next=current.next.next
        
        return dummy.next
        