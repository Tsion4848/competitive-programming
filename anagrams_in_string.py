class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        count = Counter(p)
        req = len(p)

        for r, c in enumerate(s):
            count[c] -= 1
            if count[c] >= 0:
                req -= 1
            if r >= len(p):
                count[s[r - len(p)]] += 1
                if count[s[r - len(p)]] > 0:
                    req += 1
            if req == 0:
                ans.append(r - len(p) + 1)

        return ans
