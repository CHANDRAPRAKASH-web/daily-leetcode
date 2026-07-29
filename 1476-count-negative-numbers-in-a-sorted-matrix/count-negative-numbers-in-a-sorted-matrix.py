class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        row_size=len(grid)
        column_size=len(grid[0])
        for i in range (row_size):
            for j in range(column_size):
                if grid[i][j]<0:
                    count+=1

        return count


        