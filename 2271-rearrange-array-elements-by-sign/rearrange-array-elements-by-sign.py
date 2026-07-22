class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        p,n=0,1
        a=[1]*(len(nums))

        for i in range(len(nums)):
            if nums[i]>0:
                a[p]=nums[i]
                p+=2
            else:
                a[n]=nums[i]
                n+=2

        return a

