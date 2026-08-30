class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        res=set()
        count=set()
        
        for i,num in enumerate(nums):
            if num not in count:
                count.add(num)
                res.add(num)
            elif num!=nums[i-1]:
                res.discard(num)
        return len(res)



        