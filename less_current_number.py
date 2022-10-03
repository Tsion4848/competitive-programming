class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count = count + 1
                
            print(count, end=",")
            arr.append(count)
            count = 0
        return(arr)
