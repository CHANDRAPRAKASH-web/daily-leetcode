class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        min_index=l
        if min_index==0:
            l,r=0,len(nums)-1
        elif target>=nums[0]:
            l,r=0,min_index-1
        else:
            l,r=min_index,len(nums)-1

        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return -1






       
