class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights.append(-1)
        best = 0
        for i in range(len(heights)):
          while heights[i] < heights[stack[-1]]:
            best = max(best, (heights[stack.pop()] * (i - stack[-1] - 1)))
          stack.append(i)
        return best