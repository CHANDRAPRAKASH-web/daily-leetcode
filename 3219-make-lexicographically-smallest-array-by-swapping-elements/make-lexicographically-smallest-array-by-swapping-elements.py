class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr=[]
        for i,v in enumerate(nums):
            arr.append((v,i))
        arr.sort()
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums) and arr[j][0] - arr[j-1][0] <=limit:
                j+=1
            index=[]
            for x in arr[i:j]:
                index.append(x[1])
            index.sort()
            for k in range(len(index)):
                nums[index[k]]=arr[k+i][0]
            i=j

        return nums
                        


        