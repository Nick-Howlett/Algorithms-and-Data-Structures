class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        arr = s.split(" ")
        if not arr:
            return 0
        ret = None
        i = -1
        for word in reversed(arr):
            if word != "":
                return len(word)
        return 0