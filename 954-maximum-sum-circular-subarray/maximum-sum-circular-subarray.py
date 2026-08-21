class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum=0
        cur_min=0
        max_sum=float('-inf')
        cur_max=0
        min_sum=float('inf')
        for i in nums:
            total_sum+=i
            cur_max+=i
            max_sum=max(max_sum,cur_max)
            if cur_max<0:
                cur_max=0
            cur_min+=i
            min_sum=min(min_sum,cur_min)
            if cur_min>0:
                cur_min=0

        if max_sum<0:
            return max_sum
        else:
            return max(max_sum,total_sum-min_sum)
        