class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        right_wall=n
        down_wall=m
        left_wall=-1
        up_wall=0
        res=[]
        i,j=0,0
        up,down,right,left=0,1,2,3
        direction=right
        while len(res)<m*n:
            if direction==right:
                while j<right_wall:
                    res.append(matrix[i][j])
                    j+=1
                j-=1
                right_wall-=1
                i+=1
                direction=down
            elif direction==down:
                while i<down_wall:
                    res.append(matrix[i][j])
                    i+=1
                i-=1
                direction=left
                j-=1
                down_wall-=1
            elif direction==left:
                while j>left_wall:
                    res.append(matrix[i][j])
                    j-=1
                j+=1
                direction=up
                left_wall+=1
                i-=1
            else:
                while i>up_wall:
                    res.append(matrix[i][j])
                    i-=1
                i+=1
                direction=right
                up_wall+=1
                j+=1

        return res

                
            


        