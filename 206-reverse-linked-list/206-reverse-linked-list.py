# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur,prev= head, None
        
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

            
        return prev