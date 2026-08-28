class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        left_sum=0
        right_sum=0
        for i in range(k):
            left_sum+=nums[i]
        max_sum=left_sum
        for i in range(1,k+1):
            left_sum-=nums[k-i]
            right_sum+=nums[-i]
            max_sum=max(max_sum,left_sum+right_sum)
        return max_sum

        