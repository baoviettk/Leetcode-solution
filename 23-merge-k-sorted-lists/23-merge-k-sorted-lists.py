# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result_head=ListNode(0,None)
        current=result_head
        heap=[]
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,[lists[i].val,i])
                
        while len(heap)>0:
            val,index=heappop(heap)
            current.next, current=lists[index], lists[index]
            if lists[index].next:
                lists[index]=lists[index].next
                heappush(heap,[lists[index].val,index])
                
        return result_head.next
        