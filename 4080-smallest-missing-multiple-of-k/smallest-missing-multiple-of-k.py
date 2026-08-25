class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=set(nums)
        n=1
        while True:
            if k*n not in a:
                return k*n
            n+=1

        