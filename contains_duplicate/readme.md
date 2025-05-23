
# Contains Duplicate

---

## Problem Description

You are given an array of integers. The task is to check whether the array contains any duplicates. If any value appears **more than once**, return `True`. Otherwise, return `False`.

### Example:

```python
Input: nums = [1, 2, 3, 4]
Output: False

Input: nums = [1, 2, 3, 1]
Output: True
```

---

## Solution

The solution uses a **set** to keep track of the elements we’ve already seen while iterating through the array.

### Python Code:

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

### Time Complexity:

* **O(n)** – We traverse the list once, and each lookup/add operation in a set takes constant time.

### Space Complexity:

* **O(n)** – In the worst case (no duplicates), we store every element in the set.

---

```python
sol = Solution()
print(sol.containsDuplicate([1, 2, 3, 4]))     # False
print(sol.containsDuplicate([1, 2, 3, 1]))     # True
```

---


