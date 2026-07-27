class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        a={}
        for i,val in enumerate(nums):
            if val in a:
                if abs(i-a.get(val))<=k:
                    return True
                else:
                    a[val]=i
            else:
                a[val]=i

        return False
        