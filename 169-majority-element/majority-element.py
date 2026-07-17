class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        output={}
        n=len(nums)
        for i in nums:
            output[i]=1+output.get(i,0)

        for i in nums:
            if output[i]>n/2:
                return i
        