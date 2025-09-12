/**
 * 
 * 
 */
import java.util.*;

class TwoSumII{

    // solution using two pointers
    public int[] solutionI(int[] numbers, int target){
        int left = 0;
        int right = numbers.length - 1;
        
        while (left < right){
            
            if (numbers[left] + numbers[right] == target){
                return {left + 1, right + 1};
            }
            else if(numbers[left] + numbers[right] > target){
                right -= 1;
            }
            else{
                left += 1;
            }

        }
    }

    // solution using a map
    public int[] solutionII(int[] numbers, int target){

        Map<Integer, Integer> numMap = new HashMap<>();

        for (int i = 0, i < numbers.length; i+= 1){
            int difference = target - numbers[i];
            if(numMap.containsKey(difference)){
                return {numMap.get(difference), i + 1}
            }
            numMap.put(numbers[i], i + 1);
        }

        return new int[0];
    }

}