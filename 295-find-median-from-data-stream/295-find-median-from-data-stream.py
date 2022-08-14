class MedianFinder:

    def __init__(self):
        #min for bigger half, max for smaller half
        self.max_heap, self.min_heap=[],[]
        

    def addNum(self, num: int) -> None:
        heappush(self.max_heap,-num)
        if len(self.max_heap)>len(self.min_heap)+1:
            heappush(self.min_heap, -heappop(self.max_heap))
        if len(self.min_heap)>0 and -self.max_heap[0]>self.min_heap[0]:
            heappush(self.max_heap,-heappop(self.min_heap))
            heappush(self.min_heap,-heappop(self.max_heap))

            
        

    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0]+self.min_heap[0])/2


