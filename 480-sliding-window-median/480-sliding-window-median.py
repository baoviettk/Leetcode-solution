class Solution(object):
    def __init__(self):
        self.small, self.large=[],[]
        # small is max
        # large is min
    def medianSlidingWindow(self, nums, k):
        arr=[]

        for i in range(len(nums)):
            self.addNum(nums[i])
            self.rebalance()
            if i==k-1:
                arr.append(self.findMedian())
            if i>k-1:
                removeNum= nums[i-k]
                if removeNum<self.large[0]:
                    self.removeNum(self.small, -1*removeNum)
                else:
                    self.removeNum(self.large, removeNum)
                self.rebalance()
                arr.append(self.findMedian())
        return arr
    def addNum(self, num):
        heapq.heappush(self.small,-1*num)
        
        if self.small and self.large and -1*self.small[0]>self.large[0]:
            val=-1*heapq.heappop(self.small)            
            heapq.heappush(self.large,val)
        
    def rebalance(self):
        if len(self.small)> len(self.large)+1:
            val=-1*heapq.heappop(self.small)            
            heapq.heappush(self.large,val)
        
        if len(self.large)> len(self.small)+1:
            val=heapq.heappop(self.large)            
            heapq.heappush(self.small,-1*val)
            
    def removeNum(self, heap, num):
        index= heap.index(num)
        heap[index]= heap[-1]
        del heap[-1]
        
        if index< len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)
        
    def findMedian(self):
        if len(self.small)>len(self.large):
            return -1*self.small[0]
        if len(self.small)<len(self.large):
            return self.large[0]
        return (-1*self.small[0]+ self.large[0])/float(2)
        
        
        