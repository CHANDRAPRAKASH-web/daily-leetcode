class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        count=[0]*101
        res=[]
        a=min(nums)
        b=max(nums)

        for i in nums:
            count[i]=1

        for i in range(a,b+1):
            if count[i]==0:
                res.append(i)

        return res


    
       