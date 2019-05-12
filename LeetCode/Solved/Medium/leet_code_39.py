class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.bfs(candidates, 0, target, [])
        
    
    
    def bfs(self, candidates, start, target, path):
        if target < 0:
            return []
        if target == 0:
            return [path]
        paths = []
        for i in range(start, len(candidates)):
            if target >= candidates[i]:
                paths.extend(self.bfs(candidates, i, target - candidates[i], path + [candidates[i]]))
        return paths