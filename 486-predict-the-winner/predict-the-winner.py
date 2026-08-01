class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dp(l,r):
            if l==r:
                return nums[l]
            left=nums[l]-dp(l+1,r)
            right=nums[r]-dp(l,r-1)
            return max(left,right)

        r=len(nums)-1
        return dp(0,r)>=0
    
        