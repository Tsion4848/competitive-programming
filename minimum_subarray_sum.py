class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = math.inf
        summ = 0
        j = 0

        for i, num in enumerate(nums):
            summ += num
            while summ >= target:
                res = min(res, i - j + 1)
                summ -= nums[j]
                j += 1

        return res if res != math.inf else 0
