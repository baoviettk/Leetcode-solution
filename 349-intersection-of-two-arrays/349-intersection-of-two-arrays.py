class Solution(object):
    def intersection(self, nums1, nums2):
        nums1_set= set(nums1)
        nums2_set=set(nums2)
        arr=[]
        for num in nums2_set:
            if num in nums1_set:
                arr.append(num)
        return arr
        