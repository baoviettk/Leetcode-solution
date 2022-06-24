class MedianFinder(object):

    def __init__(self):
        self.small, self.large=[],[]

        # small is max
        # large is min
    def addNum(self, num):
        heapq.heappush(self.small,-1*num)
        
        if self.small and self.large and -1*self.small[0]>self.large[0]:
            val=-1*heapq.heappop(self.small)            
            heapq.heappush(self.large,val)
        
        if len(self.small)> len(self.large)+1:
            val=-1*heapq.heappop(self.small)            
            heapq.heappush(self.large,val)
        
        if len(self.large)> len(self.small)+1:
            val=heapq.heappop(self.large)            
            heapq.heappush(self.small,-1*val)
            

    def findMedian(self):
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        return (-1*self.small[0]+ self.large[0])/float(2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()