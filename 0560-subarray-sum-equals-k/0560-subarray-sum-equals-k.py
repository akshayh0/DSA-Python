class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        # Hash map to store (prefix_sum -> frequency)
        prefix_sums = {0: 1}
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in our map, 
            # it means we found subarray(s) that sum to k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # Record the current prefix sum in the map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count
