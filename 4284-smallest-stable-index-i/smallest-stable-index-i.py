class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_value=float('inf')
        max_value=float('-inf')
        min_list=[]
        for i in range(len(nums)-1,-1,-1):
            min_value=min(min_value,nums[i])
            min_list.append(min_value)
        min_list.reverse()
        for i in range(len(nums)):
            max_value=max(nums[i],max_value)
            if max_value-min_list[i]<=k:
                return i
        return -1