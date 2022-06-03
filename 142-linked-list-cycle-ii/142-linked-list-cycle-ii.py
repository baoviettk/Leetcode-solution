# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast,slow=head,head
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            
            if fast==slow:
                break
        if fast == None or fast.next== None:
            return None
        new = head
        index=0
        while(new!=slow):
            new=new.next
            slow=slow.next
            index+=1
        
        return new