class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
          return "0"
        for j in range(k):
          for i in range(1, len(num)):
            if num[i - 1] > num[i]:
              num = num[:i - 1] + num[i:]
              break
            if i == len(num) - 1:
              num = num[:-1]
        i = 0
        while i < len(num) and num[i] == "0":
          i += 1
        retnum = num[i:]
        return retnum if len(retnum) > 0 else "0"