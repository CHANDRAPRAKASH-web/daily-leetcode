class Solution:
    def corpFlightBookings(self, nums: List[List[int]], n: int) -> List[int]:
        answer=[0]*n
        for i in nums:
            answer[i[0]-1]+=i[2]
            if i[1]<n:
                answer[i[1]]-=i[2]

        cur=0
        for i,val in enumerate(answer):
            cur+=val
            answer[i]=cur

        return answer

       
        