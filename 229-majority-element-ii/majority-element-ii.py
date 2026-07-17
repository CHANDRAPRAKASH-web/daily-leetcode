class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a={}
        b=[]
        n=len(nums)
        for i in nums:
            a[i]=1+a.get(i,0)

        for i in a:
            if a[i]>n/3:
                b.append(i)
        return b
                
        