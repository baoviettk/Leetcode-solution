class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0, len(height)-1
        max_a=0
        while l<r:
            max_a=max(min(height[l],height[r])*(r-l), max_a)
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_a