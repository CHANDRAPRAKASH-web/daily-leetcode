class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r=0,len(nums)-1
        a=[]
        while l<=r:
            if abs(nums[l])<abs(nums[r]):
                a.append(nums[r]**2)
                r-=1
            else:
                a.append(nums[l]**2)
                l+=1
        a.reverse()
        return a


        