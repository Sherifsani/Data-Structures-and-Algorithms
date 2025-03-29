# Merge Sort
Merge sort is a sorting algorithm that recursively splits an array into smaller arrays before comparing them and arranging them back into the original array.

**TIME COMPLEXITY: O(nlogn)**

## The steps
first we divide an array into two parts, left and right
```python
     mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
```