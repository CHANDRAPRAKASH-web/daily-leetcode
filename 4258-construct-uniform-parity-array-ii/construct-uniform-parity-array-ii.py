class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        return all(num%2==1 for num in nums) or all(num%2==0 for num in nums) or min(nums)%2==1
