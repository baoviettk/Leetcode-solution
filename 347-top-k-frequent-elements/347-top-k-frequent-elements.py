class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=[[] for i in range(len(nums)+1)]
        freq={}
        result=[]
        
        for num in nums:
            freq[num]= freq.get(num,0)+1
        
        for num, fre in freq.items():
            count[fre].append(num)
        
        for i in range(len(nums),-1,-1):
            for num in count[i]:
                result.append(num)
                if len(result)==k:
                    return result
        
        
        