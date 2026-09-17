class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0
            
        # Track the global maximum, and the running max/min products
        result = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]
            
            # If current element is negative, swap max and min values
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
                
            # Choose the maximum/minimum between the current element alone
            # or combining it with the previous sequence
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            
            # Update the absolute largest product found
            result = max(result, max_so_far)
            
        return result
