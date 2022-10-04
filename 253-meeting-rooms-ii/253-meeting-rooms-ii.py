class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start,end=[],[]
        res,cur=0,0
        LEN=len(intervals)
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        end.sort()
        start.sort()
        
        s,e=0,0
        while s<LEN:
            if start[s]<end[e]:
                cur+=1
                s+=1
                res=max(res,cur)
            else:
                cur-=1
                e+=1
        return res
            