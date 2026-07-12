class Solution:
    def countDigits(self, num: int) -> int:
        
        count=0
        b=num
        while num>0:
            c=num%10
            if b%c==0:
                count+=1
            num=num//10
            
        return count
        
