class Solution:
    def sumGame(self, nums: str) -> bool:
        s1,q1=0,0
        s2,q2=0,0
        n=len(nums)

        for i in range(n):
            if i<n//2:
                if nums[i]!='?':
                    s1+=int(nums[i])
                else:
                    q1+=1
            else:
                if nums[i]!='?':
                    s2+=int(nums[i])
                else:
                    q2+=1
        if (q1+q2)%2==1:
            return True
        else:
            if s1-s2==((q2-q1)//2)*9:
                return False
            else:
                return True
        