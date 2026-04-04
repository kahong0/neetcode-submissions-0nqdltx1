class Solution {
    public int[] twoSum(int[] nums, int target) {

        int n = nums.length;

        for (int i = 0; i < n; i++) 
        {  
            for (int j = i + 1; j < n; j++)
            {
            if (nums[i] + nums[j] == target)
                {
                return new int[]{i,j};
                }
            }
        }
        return new int[]{ , };
    }
}

/* 
create a for-loop and trace through each value in the array 
take the value at the first index and add it the value at the following index and see if it adds up to the target
if it doesn't add it the target continue to the next value
once you get to the end of the array, loop back to the next index and compare the rest
*/
