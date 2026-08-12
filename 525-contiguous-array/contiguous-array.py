class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zero=0
        one=0
        res=0
        diff={}

        for i,n in enumerate(nums):
            if n==0:
                zero+=1
            else:
                one+=1

            if one-zero not in diff:
                diff[one-zero]=i

            if one==zero:
                res=one+zero

            else:
                d=diff[one-zero]
                res=max(res,i-d)

        return res

       