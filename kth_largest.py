class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        nums.sort()
        
        nums = [str(i) for i in nums]
        length = len(nums)
        return nums[length - k]
