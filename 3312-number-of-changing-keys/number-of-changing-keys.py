class Solution:
    def countKeyChanges(self, s: str) -> int:
        count=0
        for i in range(0,len(s)-1):
            if s[i].lower() != s[i+1].lower():
                count+=1
        return count
        