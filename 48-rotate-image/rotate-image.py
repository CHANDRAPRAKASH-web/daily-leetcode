class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res=[[] for _ in range(len(matrix))]
        index=0
        for j in range(len(matrix[0])):
            for i in range(len(matrix)-1,-1,-1):
                res[index].append(matrix[i][j])
            index+=1
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j]=res[i][j]
        