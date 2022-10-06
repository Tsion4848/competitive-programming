class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(nums):
            if len(nums) < 2:
                return False
            
            if len(nums) == 2:
                return True
            diff = nums[1] - nums[0]
            for i in range(1, len(nums) - 1):
                if nums[i+1] - nums[i] != diff:
                    return False
            return True
        
        ans = []
        n = len(l)
        for i in range(n):
            x = nums[l[i]:r[i]+1]
            x.sort()
            if check(x):
                ans.append(True)
            else:
                ans.append(False)
                
        return ans
