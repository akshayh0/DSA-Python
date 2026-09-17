class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
            
        result = []
        
        # Initialize the four boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right along the top row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # Move the top boundary down
            
            # 2. Traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # Move the right boundary left
            
            # Check if boundaries have crossed before proceeding
            if top <= bottom:
                # 3. Traverse from right to left along the bottom row
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # Move the bottom boundary up
                
            if left <= right:
                # 4. Traverse from bottom to top along the left column
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # Move the left boundary right
                
        return result
