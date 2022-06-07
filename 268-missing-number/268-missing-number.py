class Solution(object):
    def missingNumber(self, nums):
        total_sum= (len(nums))*(len(nums)+1)/2
        print(total_sum)
        nums_sum= sum(nums)
        print(nums_sum)
        return (total_sum-nums_sum)
        