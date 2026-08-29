class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        prefix=0
        res=0
        for i in range(len(nums)-k):
            prefix=max(prefix,nums[i])
            res=max(res,prefix+nums[i+k])
        return res