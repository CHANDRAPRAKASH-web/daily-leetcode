class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        smallest_odd=float('inf')
        for i in nums:
            if i%2==1:
                smallest_odd=min(smallest_odd,i)
        if smallest_odd==float('inf'):
            return True
        for i in nums:
            if i%2==0 and i<smallest_odd:
                return False
        return True
                
       