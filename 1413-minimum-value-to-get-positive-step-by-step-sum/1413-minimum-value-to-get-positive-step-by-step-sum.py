class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        result=99999
        cur=0
        for num in nums:
            cur+=num
            result=min(cur,result)
        return 1 if result>0 else abs(result)+1