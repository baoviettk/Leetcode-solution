class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        if n==0:
            return 0
        events.sort()
        res,i=0,0
        end=[]
        while i<n or end:
            if not end:
                day=events[i][0]
            while i<n and events[i][0]==day:
                heappush(end,events[i][1])
                i+=1
            res+=1
            day+=1
            heappop(end)
            while end and day>end[0]:
                heappop(end)
        
        return res
        
        