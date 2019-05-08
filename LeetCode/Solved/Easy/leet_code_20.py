class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "}": "{", "]":"["}
        stack = []
        for bracket in s:
            if bracket in d:
                if not stack:
                    return False
                match = stack.pop()
                if d[bracket] != match:
                    return False
            else:
                stack.append(bracket)
        return len(stack) == 0