#https://leetcode.com/problems/permutations-ii/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        perms = []
        for i in range(len(nums)):
            others = self.permuteUnique(nums[:i] + nums[i + 1:])
            perms.extend([[nums[i]] + other for other in others])
        permset = set(tuple(perm) for perm in perms)
        return list(map(lambda x: list(x), permset))