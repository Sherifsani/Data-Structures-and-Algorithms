class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        
        res = [[1]]  # Initialize with the first row
        
        for i in range(1, numRows):
            prev_row = res[-1]  # Get the last row
            new_row = [1]  # First element is always 1
            
            # Middle elements: sum of two elements from the previous row
            for j in range(1, i):
                new_row.append(prev_row[j-1] + prev_row[j])
            
            new_row.append(1)  # Last element is always 1
            res.append(new_row)
        
        return res