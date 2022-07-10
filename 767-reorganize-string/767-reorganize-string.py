class Solution:
    def reorganizeString(self, s: str) -> str:
        result=""
        count=Counter(s)
        heap=[[-cnt,char] for char, cnt in count.items() ]
        
        heapify(heap)
        
        prev=None
        while prev or heap:
            if prev and not heap:
                return ""
            cnt, char= heappop(heap)
            result+=char
            cnt+=1
            
            if prev:
                heappush(heap,prev)
                prev=None
            
            if cnt!=0:
                prev=[cnt,char]
                
        return result