class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        for i in range(len(nums)):
            if nums[i]==a or nums[i]==b:
                left_res=i+1
        for i in range(1,len(nums)+1):
            if nums[-i]==a or nums[-i]==b:
                right_res=i
        for i in range(len(nums)):
            if nums[i]==a or nums[i]==b:
                left=i+1
                break
        for i in range(1,len(nums)+1):
            if nums[-i] == a or nums[-i]==b:
                right=i
                break
        return min(left_res,right_res,left+right)

        