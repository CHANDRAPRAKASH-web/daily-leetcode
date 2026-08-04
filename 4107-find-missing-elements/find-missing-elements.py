class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=set(nums)
        b,c=min(nums),max(nums)
        res=[]
        for i in range(b,c+1):
            if i not in a:
                res.append(i)

        return res
       