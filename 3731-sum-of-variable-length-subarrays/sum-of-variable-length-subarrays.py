class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        total_sum=0
        for i in range(len(nums)):
            start=max(0,i-nums[i])
            if i>0:
                nums[i]+=nums[i-1]
            if start==0:
                total_sum+=nums[i]
            else:
                total_sum+=nums[i]-nums[start-1]
        return total_sum