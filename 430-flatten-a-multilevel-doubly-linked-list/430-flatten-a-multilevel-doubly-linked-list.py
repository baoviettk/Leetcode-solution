"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        cur=head
        stk=[]
        while cur:
            if cur.child:
                if cur.next:
                    stk.append(cur.next)
                cur.next=cur.child
                cur.child.prev=cur
                cur.child=None
            if not cur.next:
                if stk:
                    nxt=stk.pop()
                    cur.next=nxt
                    nxt.prev=cur
            cur=cur.next
        return head