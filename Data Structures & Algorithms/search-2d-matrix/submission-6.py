class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, len(matrix) - 1
        while l <= h:
            mid = (h + l) // 2

            if matrix[mid][0] > target:
                h = mid - 1
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                row = mid
                break
        else:
            return False

        l, h = 0, len(matrix[row]) - 1
        while l <= h:
            mid = (h + l) // 2

            if matrix[row][mid] > target:
                h = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:

                return True

        return False