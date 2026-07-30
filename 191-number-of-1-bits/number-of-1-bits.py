class Solution:
    def hammingWeight(self, n: int) -> int:
        return format(n,'b').count('1')