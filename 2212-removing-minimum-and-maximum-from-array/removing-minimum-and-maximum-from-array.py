class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minIndex=nums.index(min(nums))
        maxIndex=nums.index(max(nums))
        
        left_res=max(minIndex,maxIndex)+1
        right_res=len(nums)-min(minIndex,maxIndex)

        left=min(minIndex,maxIndex)+1
        right=len(nums)-max(minIndex,maxIndex)

        return min(left_res,right_res,left+right)
        