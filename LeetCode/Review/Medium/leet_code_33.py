class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        left = 0
        right = len(nums) - 1
        pivot = None
        if nums[left] < nums[right]:
            return self.bsearch(nums, 0, len(nums) - 1, target)
        else:
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid + 1] < nums[mid]:
                    pivot = mid + 1
                    break
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        if nums[pivot] == target:
            return pivot
        elif target < nums[0]: 
            return self.bsearch(nums, pivot, len(nums) - 1, target)
        else:
            return self.bsearch(nums, 0, pivot - 1, target)
            
        
    
    def bsearch(self, arr, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1