class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        min_sum=float('inf')
        cur_sum=0
        for i in nums:
            cur_sum+=i
            max_sum=max(cur_sum,max_sum)
            if cur_sum<0:
                cur_sum=0
        cur_sum=0
        for i in nums:
            cur_sum+=i
            min_sum=min(cur_sum,min_sum)
            if cur_sum>0:
                cur_sum=0

        return max(abs(max_sum),abs(min_sum))
            
        