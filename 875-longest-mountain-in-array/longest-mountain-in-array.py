class Solution:
    def longestMountain(self, nums: List[int]) -> int:
        res=0
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]>nums[i+1]:
                l=i-1
                r=i+1
                while l>0 and nums[l]>nums[l-1]:
                    l-=1
                while r<len(nums)-1 and nums[r]>nums[r+1]:
                    r+=1
                res=max(res,r-l+1)
        return res
        