class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=set(jewels)
        count=0
        for i in stones:
            if i in a:
                count+=1

        return count

        