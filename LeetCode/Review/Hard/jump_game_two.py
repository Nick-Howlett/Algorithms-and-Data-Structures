class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = end = furthest = 0
        for i, num in enumerate(nums[:-1]):
            furthest = max(furthest, i + num)
            if i == end:
                jumps += 1
                end = furthest
        return jumps