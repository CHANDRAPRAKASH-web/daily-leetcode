class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix=1
        sufix=1
        max_product=float('-inf')
        n=len(nums)
        for i in range(n):
            if prefix==0:
                prefix=1
            if sufix==0:
                sufix=1
            prefix*=nums[i]
            sufix*=nums[n-i-1]
            max_product=max(max_product,max(prefix,sufix))
        return max_product
       