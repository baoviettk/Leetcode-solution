class Solution(object):
    def insert(self, intervals, newInterval):
#         if len(intervals)==0:
#             return [newInterval]
#         if intervals[0][0]>newInterval[1]:
#             intervals.insert(0,newInterval)
#             return intervals
#         if intervals[-1][1]< newInterval[0]:
#             intervals.append(newInterval)
#             return intervals
        
        arr=[]
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[1]:
                arr.append(newInterval)
                return arr+ intervals[i:]
            if intervals[i][1]<newInterval[0]:
                arr.append(intervals[i])
                
            else:
                print('here')
                newInterval= [min(intervals[i][0], newInterval[0]),max(intervals[i][1], newInterval[1])]
                
        arr.append(newInterval)
        return arr