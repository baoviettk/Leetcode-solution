class Solution(object):
    def findKthLargest(self, nums, k):
        k=len(nums)-k
        
        def quickSelect(l,r):
            ran= random.randint(l, r)
            nums[ran],nums[r]=nums[r],nums[ran]
            p,pivot=l,nums[r]
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[i], nums[p]=nums[p],nums[i]
                    p+=1
            nums[p],nums[r]=pivot, nums[p]
            if p==k: 
                return pivot
            if p<k: 
                return quickSelect(p+1,r)
            return quickSelect(l,p-1)
        
        return quickSelect(0,len(nums)-1)
        