class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
        intervals.sort()
        result=[intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]>result[-1][1]:
                result.append(intervals[i])
            elif result[-1][1]>=intervals[i][0]:
                result[-1][1]=max(result[-1][1],intervals[i][1])
        
        return result