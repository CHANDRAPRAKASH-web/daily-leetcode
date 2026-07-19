class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a=set(nums2)
        m=float('inf')
        temp=0
        for i in nums1:
            if i in a and i<m:
                m=i
                temp=1
        if temp==0:
            return -1
        return m

        
        