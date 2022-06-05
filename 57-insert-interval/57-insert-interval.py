class Solution(object):
    def insert(self, intervals, newInterval):
        if len(intervals)==0:
            return [newInterval]
        if intervals[0][0]>newInterval[1]:
            return_array=[newInterval]
            for interval in intervals:
                return_array.append(interval)
            return return_array
        current=99999
        for i in range (len(intervals)):
            if intervals[i][1]>=newInterval[0]:
                current=i
                break
        print(current)

        if current==99999:
            intervals.append(newInterval)
            return intervals
        if newInterval[1]<intervals[current][0]:
            intervals.insert(current,newInterval)
            return intervals

        intervals[current][1]=max(intervals[current][1], newInterval[1])
        intervals[current][0]=min(intervals[current][0], newInterval[0])

        next=current+1
        loop_run=False
        while next<len(intervals) and intervals[next][0]<=intervals[current][1]:
            intervals[current][1]=max(intervals[current][1], intervals[next][1])
            # intervals[current][0]=min(intervals[current][0], newInterval[0])
            del intervals[next]
        if intervals[-1][1]<newInterval[0]:
            intervals.append(newInterval[0])
        return intervals