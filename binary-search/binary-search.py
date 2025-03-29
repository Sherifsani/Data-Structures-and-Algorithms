def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            print("target found")
            return 1
        else:
            if arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return 0

print(binary_search([1,3,5,6,7], 7))