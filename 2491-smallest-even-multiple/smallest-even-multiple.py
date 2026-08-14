class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        while True:
            if (n*i)%2==0:
                return n*i
            i+=1
        