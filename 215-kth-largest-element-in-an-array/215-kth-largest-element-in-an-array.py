class Solution(object):
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i]=-1*nums[i]
        heapq.heapify(nums)
        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -1* heapq.heappop(nums)
        