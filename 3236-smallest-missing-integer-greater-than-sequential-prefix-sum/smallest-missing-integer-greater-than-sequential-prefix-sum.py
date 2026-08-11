class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix=nums[0]
        a=set(nums)
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefix+=nums[i]
            else:
                break

        while True:
            if prefix not in a:
                return prefix
            prefix+=1
        