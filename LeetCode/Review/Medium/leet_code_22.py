#Incorrect approach, needs to be fully reattempted
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            ret = []
            valids = self.generateParenthesis(n - 1)
            valid_set = ({"()" + valid for valid in valids} |
                         {"(" + valid + ")" for valid in valids} |
                         {valid + "()" for valid in valids})
            two_power = 2
            while n % two_power == 0:
                subvalids = self.generateParenthesis(n / two_power)
                subvalid_set = {subvalid * two_power for subvalid in subvalids}
                valid_set = valid_set | subvalid_set
                two_power *= 2
            return sorted(list(valid_set))