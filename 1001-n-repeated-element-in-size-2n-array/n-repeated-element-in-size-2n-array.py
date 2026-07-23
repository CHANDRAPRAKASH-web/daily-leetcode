class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        a={}
        for i in nums:
            a[i]=1+a.get(i,0)

        for i in a:
            if a[i]==n:
                return i
        