class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        b=min(nums)
        c=max(nums)
        a=set(nums)
        res=[]

        for i in range(b,c+1):
            if i not in a:
                res.append(i)

        return res

        