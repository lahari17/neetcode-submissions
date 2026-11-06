class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1
        while top <= bottom:
            mid_row = (top + bottom)//2
            row_min = matrix[mid_row][0]
            row_max = matrix[mid_row][-1]

            if target < row_min:
                bottom = mid_row-1
            elif target > row_max:
                top = mid_row + 1
            else:
                left = 0
                right = len(matrix[0])-1
                while left <=right:
                    mid_col = (left + right)//2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        left = mid_col +1
                    elif matrix[mid_row][mid_col] > target:
                        right = mid_col- 1
                return False
        return False


            