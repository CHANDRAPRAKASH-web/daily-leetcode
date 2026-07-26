class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0]*(len(height))
        max_right=[0]*(len(height))
        ml=0
        mr=0
        for i in range(1,len(height)):
            ml=max(ml,height[i-1])
            max_left[i]=ml
        for i in range(len(height)-2,-1,-1):
            mr=max(mr,height[i+1])
            max_right[i]=mr

        s=0

        for i in range(len(height)):
            d=min(max_left[i],max_right[i])-height[i]
            if d>=0:
                s+=d

        return s




        