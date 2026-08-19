class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        b=Counter(nums2)
        res=[]
        for i in nums1:
            if b[i]>=1:
                res.append(i)
                b[i]-=1
        return res

        