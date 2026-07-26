class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums)==3:
            return nums[0]*nums[1]*nums[2]
        nums.sort()
        n=len(nums)-1
        a=nums[n]*nums[n-1]*nums[n-2]
        b=nums[0]*nums[1]*nums[n]
        if a>b:
            return a
        else:
            return b

