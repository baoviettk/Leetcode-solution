class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start=[]
        end=[]
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        print(start)
        print(end)
        s,e=0,0
        cur,result=0,0
        while s<len(intervals):
            if start[s]<end[e]:
                cur+=1
                s+=1
            else:
                cur-=1
                e+=1
            result=max(cur,result)
        
        return result