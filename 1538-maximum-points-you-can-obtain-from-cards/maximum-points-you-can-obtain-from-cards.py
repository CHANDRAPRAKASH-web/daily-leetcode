class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        left_sum=0
        right_sum=0
        for i in range(k):
            left_sum+=nums[i]
        max_sum=left_sum
        n=len(nums)
        a=k-1
        for i in range(len(nums)-1,len(nums)-k-1,-1):
            right_sum+=nums[i]
            left_sum-=nums[a]
            max_sum=max(max_sum,right_sum+left_sum)
            a-=1
        return max_sum

        