class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        prev=0

        for i in nums:
            count[i]+=1


        for i in range(101):
            temp=count[i]
            count[i]=prev
            prev+=temp

        return [count[i] for i in nums]
     

      