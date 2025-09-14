import java.util.*;

/**
 * My approach
 * 1. Sort the input array to handle duplicates better
 * 2. Iterate through the array, for each element, use two pointers approach to find pairs that sum to zero (i + left + right = 0)
 * 3. The final while loop is to skip duplicates for the left pointer after a valid triplet is found
 * 4. Time complexity O(n**2)
 * 5. Space complexity O(1) if we don't consider the output list
 */


public class ThreeSum {

    public static List<List<Integer>> solution(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 1; i++) {
            if (i == 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = 1 + 1;
            int right = nums.length - 1;
            while (left < right) {
                int sum = nums[i] + nums[left] + nums[right];
                if (sum > 0) {
                    right -= 1;
                } else if (sum < 0) {
                    left += 1;
                } else {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left += 1;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left += 1;
                    }
                }
            }
        }
        return result;
    }
}