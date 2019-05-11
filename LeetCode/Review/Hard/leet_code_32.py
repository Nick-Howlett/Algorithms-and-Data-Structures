#Bad approach, use indices instead to check length of current substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        d = {")": "(", "}": "{", "]" : "["}
        stack = []
        count = 0
        best = 0
        for bracket in s:
            if bracket in d:
                if not stack or stack.pop()[0] != d[bracket]:
                    if count > best:
                        best = count
                    count = 0
                else:
                    count += 2
                    print(count)
            else:
                stack.append((bracket, count))
        if stack:
            prev_count = stack.pop()[1]
            if prev_count > best:
                best = prev_count
            count -= prev_count
        return max(count, best)