class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        minimum=float('inf')
        res=[]
        for i in range(1,len(nums)):
            ad=nums[i]-nums[i-1]
            if ad==minimum:
                res.append([nums[i-1],nums[i]])
            elif ad<minimum:
                minimum=ad
                res=[]
                res.append([nums[i-1],nums[i]])
        return res


        
        