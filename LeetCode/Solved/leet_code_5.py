class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
          oddstr = self.extend(s, i, i)
          evenstr = self.extend(s, i, i + 1)
          maxstr = oddstr if len(oddstr) > len(evenstr) else evenstr
          if len(maxstr) > len(longest):
            longest = maxstr
        return longest
              
        
    
    
    def extend(self, string, start1, start2):
      if start2 >= len(string) or string[start1] != string[start2]:
        return ""
      step = 0
      while start1 - (step + 1) >= 0 and start2 + (step + 1) < len(string) and string[start1 - (step + 1)] == string[start2 + (step + 1)]:
        step += 1
      return string[start1 - step: start2 + step + 1]