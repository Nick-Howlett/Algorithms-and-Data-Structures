# O(n**2) solution, can do O(n).
class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        for i in range(len(height)):
          for j in range(i, len(height)):
            area = (j - i) * min(height[i], height[j])
            if area > best: best = area
        return best
