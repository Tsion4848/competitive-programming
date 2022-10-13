class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]

        curSum = 0
        for i in range(len(nums)):
            if (curSum == sum - curSum - nums[i]):
                return i;
            curSum += nums[i]
        return -1
