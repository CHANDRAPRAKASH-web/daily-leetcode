class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[float('inf'),float('-inf')]
        n=(len(nums)//2)-1
        l=0
        r=n+1
        count=0
        while r<len(nums):
            if nums[l]==target and l<=n and l>=0:
                res[0]=min(res[0],l)
                res[1]=max(res[1],l)
                count+=1

            if nums[r]==target:
                res[0]=min(res[0],r)
                res[1]=max(res[1],r)
                count+=1

            l+=1
            r+=1


        if count==0:
            return [-1,-1]
        else:
            return res
                




        