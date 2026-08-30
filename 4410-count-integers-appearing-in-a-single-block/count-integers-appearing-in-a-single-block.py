class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        seen = set()
        special = set()
        
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                special.add(num)
            elif nums[i - 1] != num:
                # If seen before but not immediately preceding, it's split into multiple blocks
                special.discard(num)
                
        return len(special)