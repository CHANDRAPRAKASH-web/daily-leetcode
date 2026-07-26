class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        a=[1]*(len(nums))
        for i in range(len(nums)):
            a[i]=nums[nums[i]]

        return a
        