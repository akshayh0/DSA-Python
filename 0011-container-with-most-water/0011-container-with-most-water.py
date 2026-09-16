class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            # Calculate the current width and limiting height
            width = right - left
            current_height = min(height[left], height[right])
            
            # Calculate water volume and update max_water if it's larger
            current_water = width * current_height
            if current_water > max_water:
                max_water = current_water
            
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
