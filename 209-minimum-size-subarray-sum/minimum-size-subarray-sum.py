class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        length=float("inf")
        prefix=0
        for r in range(len(nums)):
            prefix+=nums[r]
            while prefix>=target:
                length=min(length,r-l+1)
                prefix-=nums[l]
                l+=1
        return 0 if length==float('inf') else length

        