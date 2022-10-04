class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        j = 0

        while j < length - 1:

            if (nums[j] > nums[j + 1]):

                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp


                j = -1
            j += 1

            print(nums)
