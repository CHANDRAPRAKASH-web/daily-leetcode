class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=[0]*101
        a={}
        res=[]
        prev=0

        for i in nums:
            count[i]+=1

        for i in range(101):
            if count[i]>0:
                a[i]=prev
                prev+=count[i]

        for i in nums:
            res.append(a[i])


        return res

       


        

       
      