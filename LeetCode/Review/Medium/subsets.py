class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        subs = self.subsets(nums[1:])
        return [[nums[0]] + sub for sub in subs] + subs