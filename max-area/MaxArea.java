/**
 * Approach: (Two pointers)
 * 1. Initialize two pointers, one at the start (left) and one at the end (right) of the array
 * 2. Calculate the area formed between the two pointers and update the maximum area if the current area is larger
 * 3. Move the left pointer inward if the height at the left pointer is less than the height at the right pointer, otherwise move the right pointer inward
 * 4. Repeat steps 2-3 until the two pointers meet
 * 5. Time complexity O(n)
 */

public class MaxArea {
    
    public static int solutionI(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxArea = 0;

        while (left < right) {
            int currentArea = (right - left) * Math.min(left, right);
            maxArea = Math.max(currentArea, maxArea);

            if (left < right) {
                left += 1;
            } else {
                right -= 1;
            }
        }
        return maxArea;
    }
}
