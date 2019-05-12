class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_found = False
        for i, num in enumerate(nums):
            if num == 1:
                one_found = True
            if num < 1 or num > len(nums):
                nums[i] = 1
        if not one_found: return 1
        for num in nums:
            num = abs(num)
            nums[num - 1] = -abs(nums[num - 1])
        for i in range(1, len(nums)):
            if nums[i] > 0:
                return i + 1
        return len(nums) + 1