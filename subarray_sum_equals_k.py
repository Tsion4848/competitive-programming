class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pre = 0
        count = Counter({0: 1})

        for num in nums:
            pre += num
            res += count[pre - k]
            count[pre] += 1

        return res
