class MinStack:

    def __init__(self):
        self.stk=[]
        self.min_stack=[]
        

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        elif self.min_stack[-1]<val:
            self.min_stack.append(self.min_stack[-1]) 
        else:
            self.min_stack.append(val)   

    def pop(self) -> None:
        self.stk.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stk[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]

# time complexity : O(1)
# space complexity : O(N)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()