class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a={}
        for i,val in enumerate(nums):
            if val in a and i-a[val] <= k:
                return True
            a[val]=i
           
           

        return False
        