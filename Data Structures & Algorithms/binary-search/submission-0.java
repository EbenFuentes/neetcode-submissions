/*

    1. init low/left to the beginning of array
    2. init high/right to end of array
    3. while high >= low...
        4. init a mid pointer = (high + low) / 2
        5. check if target < middle # of array
            if it is, high = mid - 1, search in left half of array
        6. check if target == nums[mid], target equals middle #
            if it does, return the mid #
        7. else, search in right half of array
            low = mid + 1

    8. return -1, if loop ends we have found no  
*/


class Solution {
    public int search(int[] nums, int target) {

        
        int low = 0; // start of arr, left side
        int high = nums.length - 1; // end of arr, right side

        while(high >= low) { // when high is >= to low, we have searched entire arr
            int mid = (high + low) / 2; // this gives us the midpoint
            if(target < nums[mid]) { // check left half of array
                high = mid - 1; // if true, search in left half of array
            } else if(target == nums[mid]) { // if target == mid #, return it
                return mid;
            } else // else, search in right half of array, low = mid + 1
                low = mid + 1;
        }

        return -1; // we have searched the entire array, a target does not exist, return -1
        
    }
}
