class Solution:
    def smallestPalindrome(self, s: str) -> str:
       
        p=len(s)//2
        base=sorted(s[:p])
        if len(s)%2==1:
            a=[s[p]]
        else:
            a=[]
        reverse_base=base[::-1]

        return "".join(base+a+reverse_base)
        