from  sortedcontainers import SortedList

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=0
        left,right=SortedList(), SortedList(rating)
        
        for num in rating:
            right.remove(num)
            low_l,high_l=self.findLowHigh(left,num)
            low_r,high_r=self.findLowHigh(right,num)
            left.add(num)

            result+=low_l*high_r+high_l*low_r
        
        return result
        
    def findLowHigh(self, arr, num):
        low=arr.bisect(num)
        return low, len(arr)-low
    