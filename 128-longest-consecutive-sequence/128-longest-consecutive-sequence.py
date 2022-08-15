class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        result=0
        for n in s:
            if n-1 not in s:
                leng=1
                while n+leng in s:
                    leng+=1
                result=max(result,leng)
        return result