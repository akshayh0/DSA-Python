class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Sort the array to easily handle duplicates and use two pointers
        nums.sort()
        res = []
        
        for i in range(len(nums) - 2):
            # Skip the same element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # If the current smallest number is greater than 0, 
            # no three numbers can sum up to 0 anymore
            if nums[i] > 0:
                break
                
            # Initialize two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # Need a larger sum
                elif total > 0:
                    right -= 1  # Need a smaller sum
                else:
                    # Found a valid triplet
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # Move both pointers inward
                    left += 1
                    right -= 1
                    
        return res
