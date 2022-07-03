class Solution(object):
    def findClosestElements(self, arr, k, x):
        left,right=0,len(arr)-k
        while left<right:
            middle = (left+right)/2
            if (x-arr[middle])<=(arr[middle+k]-x):
                right=middle
            else:
                left=middle+1
        
        return arr[left:left+k]
                