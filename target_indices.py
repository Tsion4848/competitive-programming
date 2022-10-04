class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = nums.count(target)
        less = sum(n < target for n in nums)
        return [x for x in range(less, less + count)]
