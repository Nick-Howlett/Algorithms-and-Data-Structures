class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ones = set()
        twos = {}
        threes = []
        for num in nums:
            for partial_sum in twos:
                if partial_sum + num == 0:
                    for el in twos[partial_sum]:
                      new_set = {num, *el}
                      if all(new_set != el for el in threes): threes.append(new_set)
            for one in ones:
                twos[one + num] = twos.get(one + num, []) + [[one, num]]
            ones.add(num)
        return [list(three_set) for three_set in threes]