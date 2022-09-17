# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy=ListNode(0,head)
        dup=set()
        app=set()
        cur=head
        while cur:
            if cur.val in app:
                dup.add(cur.val)
            else:
                app.add(cur.val)
            
            cur=cur.next
            
        cur=dummy
        while cur:
            nxt=cur.next
            while nxt and nxt.val in dup:
                nxt=nxt.next
            cur.next=nxt
            cur=cur.next
            
        return dummy.next