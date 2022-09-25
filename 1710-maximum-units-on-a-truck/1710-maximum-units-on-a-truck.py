class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        cnt={}
        quantity=[0]*1001
        result=0
        # for [box,unit] in boxTypes:
        #     cnt[unit]=cnt.get(unit,0)+box
        for [box,unit] in boxTypes:
            quantity[unit]+=box
        for unit in range(1000,0,-1):
            if truckSize<=quantity[unit]:
                return result+unit*truckSize
            result+=unit*quantity[unit]
            truckSize-=quantity[unit]
        return result