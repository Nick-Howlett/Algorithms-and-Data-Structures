class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = [[] for i in range(n + 1)]
        memo[0] = ['']
        for i in range(1, n + 1):
            for j in range(i):
                memo[i] += ['(' + x + ')' + y for x in memo[i - j - 1] for y in memo[j]]
        return memo[n]