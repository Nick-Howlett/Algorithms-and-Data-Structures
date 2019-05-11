class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        k = len(words[0])
        ret = []
        for i in range(len(s) - k * len(words) + 1):
            start_i = i
            copy = d.copy()
            j = i + k
            l = 0
            while l < len(words) and j < len(s) + 1:
                segment = s[i:j]
                if segment not in copy:
                    break
                copy[segment] -= 1
                if copy[segment] == 0:
                    del copy[segment]
                j += k
                i += k
                l += 1
            if not copy:
                ret.append(start_i)
        return ret