import string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        alphabet = list(string.ascii_lowercase)
        prime_map = {char: prime for char, prime in zip(alphabet, primes)}
        print(prime_map)
        d = {}
        for s in strs:
            product = 1
            for char in s:
                product *= prime_map[char]
            d[product] = d.get(product, []) + [s]
        return [v for k, v in d.items()]