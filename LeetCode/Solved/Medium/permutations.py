#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        perms = []
        for i in range(len(nums)):
            others = self.permute(nums[:i] + nums[i + 1:])
            perms.extend([[nums[i]] + other for other in others])
        return perms