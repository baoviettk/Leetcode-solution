# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1,stk2=[],[]
        cur1,cur2=l1,l2
        while cur1:
            stk1.append(cur1)
            cur1=cur1.next
        while cur2:
            stk2.append(cur2)
            cur2=cur2.next
        car=0
        prev=None
        while stk1 or stk2:
            sm=car
            if stk1: 
                sm+=stk1.pop().val
            if stk2: 
                sm+=stk2.pop().val
            new= ListNode(sm%10, prev)
            car=sm//10
            prev=new
        if car:
            new= ListNode(1, prev)
        return new