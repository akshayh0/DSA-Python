class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total_sum = 0
        
        # Variables for standard Kadane (Maximum Subarray)
        max_sum = nums[0]
        current_max = 0
        
        # Variables for inverted Kadane (Minimum Subarray)
        min_sum = nums[0]
        current_min = 0
        
        for num in nums:
            total_sum += num
            
            # Find maximum subarray sum
            current_max = max(num, current_max + num)
            max_sum = max(max_sum, current_max)
            
            # Find minimum subarray sum
            current_min = min(num, current_min + num)
            min_sum = min(min_sum, current_min)
            
        # If all numbers are negative, max_sum will hold the maximum single element.
        # total_sum == min_sum means the minimum subarray takes the entire array.
        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum
