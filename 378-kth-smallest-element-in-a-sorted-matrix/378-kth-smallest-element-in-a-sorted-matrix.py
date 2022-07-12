class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result_head=ListNode(0,None)
        current=result_head
        heap=[]
        kth=0
        n=len(matrix)
        i_arr=[0]*len(matrix)
        for i in range(n):
                heappush(heap,[matrix[i][i_arr[i]],i])
                i_arr[i]+=1
                
        while len(heap)>0:
            val,index=heappop(heap)
            kth+=1
            if kth==k:
                return val
            if i_arr[index]<n:
                heappush(heap,[matrix[index][i_arr[index]],index])
                i_arr[index]+=1
                
            