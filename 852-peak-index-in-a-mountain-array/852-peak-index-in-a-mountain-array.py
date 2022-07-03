class Solution(object):
    def peakIndexInMountainArray(self, arr):
        left,right=0, len(arr)-1
        while left<=right:
            middle=(left+right)//2
            if arr[middle]>arr[middle-1] and arr[middle]>arr[middle+1]:
                return middle
            
            if arr[middle]>arr[middle-1] and arr[middle]<arr[middle+1]:
                left=middle
            else:
                right=middle
        return left
        