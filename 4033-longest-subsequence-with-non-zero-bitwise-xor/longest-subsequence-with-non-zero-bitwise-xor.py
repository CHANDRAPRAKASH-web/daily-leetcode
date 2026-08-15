class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total=0
        temp=0 # to check if any non zero number in nums
        for i in nums:
            total=total^i
            if i!=0:
                temp=1
        if temp==0:  # if all elements in nums are zero
            return 0
        if total!=0:
            return len(nums)
        else:
            return len(nums)-1
        

        