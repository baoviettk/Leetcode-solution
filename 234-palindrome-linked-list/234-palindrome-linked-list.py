# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        middle= self.findMiddle(head)
        new_head=self.reverseLinkList(middle)

        current_left=head
        current_right=new_head
        count=0
        while current_right!=middle:
            if current_left.val!=current_right.val:
                return False
            current_right=current_right.next
            current_left=current_left.next
        if current_left.val!=current_right.val:
            return False
        return True
        
    def findMiddle(self, head):
        fast,slow= head,head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        
        return slow
    
    def reverseLinkList(self, head):
        current= head
        previous=None
        
        while current!=None:
            next=current.next
            current.next=previous
            previous=current
            current=next
        
        return previous