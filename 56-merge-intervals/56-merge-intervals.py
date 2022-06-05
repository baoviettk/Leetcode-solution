class Solution(object):
    def merge(self, intervals):
        intervals.sort(key= lambda i:i[0])
        output=[intervals[0]]
        
        for interval in intervals[1:]:
            current=output[-1]
            if current[1]>=interval[0]:
                output[-1][1]= max(output[-1][1],interval[1])
            else:
                output.append(interval)
        return output