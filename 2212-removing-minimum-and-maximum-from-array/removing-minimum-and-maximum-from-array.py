class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        a=min(nums)
        b=max(nums)
        for i in range(len(nums)):
            if nums[i]==a or nums[i]==b:
                left_res=i+1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==a or nums[i]==b:
                right_res=len(nums)-i
        left=float('inf')
        right=float('inf')
        for i in range(1,len(nums)+1):
            if nums[i-1]==a or nums[i-1]==b:
                left=min(left,i-1+1)
            if nums[-i]==b or nums[-i]==a:
                right=min(right,i)
        return min(left_res,right_res,left+right)

            
        