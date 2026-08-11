class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={')':'(','}':'{',']':'['}
        stk=[]
        for i in s:
            if i not in hashmap:
                stk.append(i)

            else:
                if not stk:
                    return False
                else:
                    popped=stk.pop()
                    if hashmap[i]!=popped:
                        return False

        return not stk


        
                        

        