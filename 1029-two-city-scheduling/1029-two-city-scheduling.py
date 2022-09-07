class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        dif=[]
        result=0
        LEN=len(costs)
        for i in range(LEN):
            dif.append([costs[i][1]-costs[i][0], i])
        dif.sort()
        for i in range(LEN//2):
            result+=costs[dif[i][1]][1]
        for i in range(LEN//2, LEN):
            result+=costs[dif[i][1]][0]
            
        return result
    
    # time:O(NlogN)
    # space: O(N)