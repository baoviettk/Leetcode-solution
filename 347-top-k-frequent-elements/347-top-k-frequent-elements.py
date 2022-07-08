class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        heap=[]
        result=[]
        for num in nums:
            if num not in dic.keys():
                dic[num]=1
            else:
                dic[num]+=1
                
        for key in dic.keys():
            
            heap.append([-dic[key],key])
        
        heapify(heap)
        for _ in range(k):
            result.append(heappop(heap)[1])
        
        return result