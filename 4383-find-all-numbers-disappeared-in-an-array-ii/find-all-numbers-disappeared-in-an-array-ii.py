class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:
        a=set(nums)
        res=[]
        start=lower
        for i in range(lower,upper+1):
            if i in a:
                if i!=start:
                    res.append([start,i-1])
                start=i+1
            elif i==upper:
                res.append([start,i])
        return res
        