class Solution {
    public int minIncrementForUnique(int[] nums) {
        if(nums == null || nums.length == 0){
              return 0;
          }
          
          Arrays.sort(nums);
          int result = 0;
          int pre = nums[0];
          for(int i = 1; i < nums.length; i++){
             int nex = pre + 1;
             result += Math.max(nex - nums[i], 0);
             pre = Math.max(nex, nums[i]);
         }
         
         return result;
    }
}
