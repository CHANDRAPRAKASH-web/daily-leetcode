class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        nums.sort()
        n=len(nums)-1
        for i,val in enumerate(nums):
            if i>0 and val==nums[i-1]:
                continue
            if val>0:
                break
            l,r=i+1,n
            while l<r:
                threesum=val+nums[l]+nums[r]
                if threesum>0:
                    r-=1
                elif threesum<0:
                    l+=1
                else:
                    res.append([val,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

        return res

            
        