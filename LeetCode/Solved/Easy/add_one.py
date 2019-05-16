class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = True
        i = len(digits) - 1
        while carry and i >= 0:
            digits[i] += carry
            carry = False
            if digits[i] >= 10:
                digits[i] = 0
                carry = True
            i -= 1
        return [1] + digits if carry else digits