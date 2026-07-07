class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num={} #val = key
        for i , n in enumerate(nums):
            diff = target-n
            if diff  in hash_num:
                return [hash_num[diff],i]
            hash_num[n]=i