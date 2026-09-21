class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Sort the array to use the two-pointer technique
        nums.sort()
        closest_sum = float('inf')
        
        for i in range(len(nums) - 2):
            # Two pointers initialization
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match, return it immediately
                if current_sum == target:
                    return current_sum
                
                # Update closest_sum if current_sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on the comparison with target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
