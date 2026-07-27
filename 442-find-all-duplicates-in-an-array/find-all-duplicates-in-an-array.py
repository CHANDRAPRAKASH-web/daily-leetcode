class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        a={}
        output=[]
        for i in nums:
            a[i]=1+a.get(i,0)
        
        for i in a:
            if a[i]>1:
                output.append(i)

        return output

        