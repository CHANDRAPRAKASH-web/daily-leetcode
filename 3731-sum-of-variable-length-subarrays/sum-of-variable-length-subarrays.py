class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix=[]
        cur=0
        for i in nums:
            cur+=i
            prefix.append(cur)

        total_sum=0

        for i,val in enumerate(nums):
            right=i
            left=max(0,i-val)
            if left==0:
                total_sum+=prefix[right]
            else:
                total_sum+=prefix[right]-prefix[left-1]

        return total_sum

        