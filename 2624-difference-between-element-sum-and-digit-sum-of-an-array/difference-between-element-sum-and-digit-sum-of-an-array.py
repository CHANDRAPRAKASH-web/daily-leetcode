class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        e_sum,d_sum=0,0
        for i in nums:
            e_sum+=i
            while i>0:
                c=i%10
                d_sum+=c
                i=i//10
        return abs(e_sum-d_sum)

        