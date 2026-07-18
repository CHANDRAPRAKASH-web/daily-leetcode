class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            a[i]=1+a.get(i,0)

        for i in a:
            if a[i]>1:
                return i
        