class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]):
          return False
        left, right = 0, len(matrix)
        while left < right:
          mid = (left + right) // 2
          if matrix[mid][0] > target:
            right = mid
          else:
            left = mid + 1
        row = left - 1
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
          mid = left + (right - left) // 2
          if matrix[row][mid] == target:
            return True
          elif matrix[row][mid] > target:
            right = mid - 1
          else:
            left = mid + 1
        return False