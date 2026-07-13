class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output={}

        for i,val in enumerate(numbers):
            if target-val in output:
                return [output[target-val],i+1]
            output[val]=i+1
            
        
        




    
        