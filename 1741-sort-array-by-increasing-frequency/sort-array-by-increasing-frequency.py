class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a={}
        for i in nums:
            a[i]=1+a.get(i,0)

       
        count = [[] for _ in range(len(nums) + 1)]

        for key,val in a.items():
            count[val].append(key)

        res=[]

        for i in range(1,len(count)):
            if count[i]:
                count[i].sort(reverse=True)
                for nums in count[i]:
                    res.extend([nums] * i)


        return res



        


        

        