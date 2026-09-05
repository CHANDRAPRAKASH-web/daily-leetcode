class Solution:
    def minTimeToVisitAllPoints(self, nums: List[List[int]]) -> int:
        if len(nums)<=1:
            return 0
        res=0
        for i in range(1,len(nums)):
            a=abs(nums[i][0]-nums[i-1][0])
            b=abs(nums[i][1]-nums[i-1][1])
            res+=max(a,b)
        return res



        