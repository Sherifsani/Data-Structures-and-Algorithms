def diagonalDifference(arr):
    n = len(arr)
    left_diagonal = 0
    right_diagonal = 0
    
    for i in range(n):
        left_diagonal += arr[i][i]        # Main diagonal
        right_diagonal += arr[i][n-1-i]   # Anti-diagonal
    
    return abs(left_diagonal - right_diagonal)
