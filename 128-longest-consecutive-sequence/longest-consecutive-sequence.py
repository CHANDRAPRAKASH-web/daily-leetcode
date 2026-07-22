class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a=set(nums)
        largest=0
        for i in a:
            if i-1 not in a:
                current=i
                streak=1

                while current+1 in a:
                    current+=1
                    streak+=1

                largest=max(largest,streak)


        return largest
            


        