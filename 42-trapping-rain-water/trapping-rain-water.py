class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0
        leftmax,rightmax=height[l],height[r]
        while l<r :
            if rightmax<leftmax:
                r-=1
                rightmax=max(height[r],rightmax)
                res+=rightmax-height[r]
            else:
                l+=1
                leftmax=max(height[l],leftmax)
                res+=leftmax-height[l]
           

        return res

           