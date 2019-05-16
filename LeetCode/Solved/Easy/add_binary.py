class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            carry, digit = divmod(int(a[i]) + int(b[j]) + carry, 2)
            ret.append(str(digit))
            i -= 1
            j -= 1
        while i >= 0:
            carry, digit = divmod(int(a[i]) + carry, 2)
            ret.append(str(digit))
            i -= 1
        while j >= 0:
            carry, digit = divmod(int(b[j]) + carry, 2)
            ret.append(str(digit))
            j -= 1
        ret.reverse()
        ret = "".join(ret)
        return "1" + ret if carry else ret