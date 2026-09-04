class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        mx=float('-inf')
        suffix=[0]*n
        suffix[n-1]=nums[-1]
        for i in range(n-2,-1,-1):
            suffix[i]=min(suffix[i+1],nums[i])
        for i in range(n):
            mx=max(mx,nums[i])
            if mx-suffix[i]<=k:
                return i
        return -1

        