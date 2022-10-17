class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int prev = 0, curr = 0, maxCount = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == 1)
                curr++;
            else{
                maxCount = max(maxCount, curr + prev);
                prev = curr;
                curr = 0;
            }
        }
        maxCount = max(maxCount, curr + prev);
        return maxCount == nums.size() ? maxCount - 1 : maxCount;
        
    }
};
