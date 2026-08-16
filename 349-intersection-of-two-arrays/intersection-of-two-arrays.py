class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=set(nums2)
        res=set()

        for i in nums1:
            if i in a:
                res.add(i)

        return list(res)
        