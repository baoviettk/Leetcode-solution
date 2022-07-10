class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        dic={}
        heap=[]
        result=[]
        count= Counter(arr)
        heap=[[cnt] for num, cnt in count.items()]
        heapify(heap)
        val=heappop(heap)[0]
        while(k>=val and k!=0):
            k-=val
            if len(heap)==0:
                return 0
            val=heappop(heap)[0]
            
        return len(heap)+1