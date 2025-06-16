## productExceptSelf

### problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

### My solution:
- Iterate through the nums array and keep track of the product(excluding zeros) and the number of zeros
- A second interation to:
  - append the product / item by index (if no zeros)
  - append all zeros if zero_count is greater than 1
  - append zero to all indices except the zero index if zero is exactly 1