class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize both the current subarray sum and max sum seen so far
        # with the first element of the array
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the rest of the array starting from the second element
        for i in range(1, len(nums)):
            # Decide whether to add the current element to the existing subarray
            # or start a brand new subarray from the current element
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the maximum sum found so far
            max_sum = max(max_sum, current_sum)
            
        return max_sum
