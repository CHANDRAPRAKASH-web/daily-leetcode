class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur_max=0
        cur_min=0
        max_sum=float('-inf')
        min_sum=float('inf')
        for i in nums:
            cur_max+=i
            max_sum=max(cur_max,max_sum)
            if cur_max<0:
                cur_max=0
            cur_min+=i
            min_sum=min(min_sum,cur_min)
            if cur_min>0:
                cur_min=0

        return max(abs(max_sum),abs(min_sum))
            
        