class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        result=[]
        for x,y in points:
            heap.append([x**2+y**2,x,y])
            
        heapify(heap)
        for _ in range(k):
            d, x,y= heappop(heap)
            result.append([x,y])
        
        return result