class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        current = 0
        end = len(nums) - 1
        while current <= end:
          if nums[current] == 0:
            nums[start], nums[current] = nums[current], nums[start]
            current += 1
            start += 1
          elif nums[current] == 2:
            nums[current], nums[end] = nums[end], nums[current]
            end -= 1
          else:
            current += 1
        