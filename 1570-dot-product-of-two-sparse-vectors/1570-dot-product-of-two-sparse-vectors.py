class SparseVector:
    def __init__(self, nums: List[int]):
        self.d={}
        for i, num in enumerate(nums):
            if nums[i]!=0:
                self.d[i]=nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for i in self.d:
            if i in vec.d:
                res+=self.d[i]*vec.d[i]
        
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)