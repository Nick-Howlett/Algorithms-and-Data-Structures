class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = self.bsearch(nums, target, True), self.bsearch(nums, target, False)
        return [left, right] if left <= right else [-1, -1]
    
    def bsearch(self, nums, target, before):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if (before and target > nums[mid]) or (not before and target >= nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return left if before else right