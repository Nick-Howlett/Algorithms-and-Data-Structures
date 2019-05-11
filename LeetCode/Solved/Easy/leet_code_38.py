class Solution:
    def countAndSay(self, n: int) -> str:
        ret = "1"
        i = 1
        while i < n:
            count = 1
            prev = ret[0]
            buffer = []
            for char in ret[1:]:
                if char == prev:
                    count += 1
                else:
                    buffer.append(str(count))
                    buffer.append(prev)
                    count = 1
                prev = char
            buffer.append(str(count))
            buffer.append(prev)
            ret = "".join(buffer)
            i += 1
        return ret