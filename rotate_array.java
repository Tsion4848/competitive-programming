class Solution {
    public void rotate(int[] nums, int k) {
       if (k==0) return;
       if (nums == null || nums.length == 0) return;

       int[] result = new int[nums.length];
        
       for (int i=0; i<nums.length; i++) {
          int newInd = (i + k) % nums.length;
          result[newInd] = nums[i];
       }

       for (int i=0; i<nums.length; i++) {
          nums[i] = result[i];
    }
  }
}
