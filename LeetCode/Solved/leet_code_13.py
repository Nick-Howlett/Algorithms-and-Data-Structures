class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        ret = 0
        i = 0
        while i + 1 < len(s):
          sub = s[i:i+2]
          if sub in d:
            ret += d[sub]
            i += 2
          else:
            ret += d[sub[0]]
            i += 1
        if i == len(s) - 1: ret += d[s[i]]
        return ret