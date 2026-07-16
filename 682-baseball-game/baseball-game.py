class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a = []
        for val in operations:
            if val == "+":
                # Add the sum of the last two scores
                a.append(a[-1] + a[-2])
            elif val == "D":
                # Double the last score
                a.append(2 * a[-1])
            elif val == "C":
                # Remove the last score
                a.pop()
            else:
                # It's an integer (can be negative or multi-digit)
                a.append(int(val))
        
        return sum(a)