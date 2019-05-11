class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret  = []
        for i, num in enumerate(candidates):
            j = 1
            while num * j <= target:
                base = [num] * j
                others = []
                if i != len(candidates) - 1 or target - num != 0:
                    others = self.combinationSum(candidates[i + 1:], target - num * j)
                if num * j == target: ret.append(base)
                ret.extend([base + other for other in others])
                j += 1
        return ret