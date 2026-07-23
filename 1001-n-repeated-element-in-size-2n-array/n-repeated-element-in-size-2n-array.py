class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            if i in a:
                return i
            a.add(i)