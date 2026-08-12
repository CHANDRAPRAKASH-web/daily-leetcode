class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        a={}
        l=0
        r=0
        max_length=0

        for r in range(len(nums)):
            a[nums[r]]=1+a.get(nums[r],0)
            while a[nums[r]]>k:
                a[nums[l]]-=1
                l+=1

            max_length=max(max_length,r-l+1)

        return max_length
           
               