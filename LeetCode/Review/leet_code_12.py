#Fast but there is a more elegant one pass solution.
class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        ret = []
        keys = list(d.keys())[::-1]
        while num > 0:
          for key in keys:
            if key <= num:
              num -= key
              ret += d[key]
              break
        return "".join(ret)
