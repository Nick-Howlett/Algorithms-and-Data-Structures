class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.bfs(candidates, 0, target, [])
        
    
    
    def bfs(self, candidates, start, target, path):
        if target == 0:
            return [path]
        paths = []
        for i in range(start, len(candidates)):
            if (i == start or candidates[i] != candidates[i - 1]):
                if candidates[i] > target:
                    break
                paths.extend(self.bfs(candidates, i + 1, target - candidates[i], path + [candidates[i]]))
        return paths