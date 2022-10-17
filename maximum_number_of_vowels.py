class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        maxim = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i, c in enumerate(s):
            if c in vowels:
                maxim += 1
            if i >= k and s[i - k] in vowels:
                maxim -= 1
            res = max(res, maxim)

        return res
