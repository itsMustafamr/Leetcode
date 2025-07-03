from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                if matrix[i][j] == target:
                    return True
            
        return False
        

#proper i think
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == target:
                    return True
        return False