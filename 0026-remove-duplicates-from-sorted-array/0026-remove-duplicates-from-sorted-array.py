class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        # Pointer to place the next unique element
        write_index = 1
        
        # Iterate through the array starting from the second element
        for read_index in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[read_index] != nums[read_index - 1]:
                nums[write_index] = nums[read_index]
                write_index += 1
                
        # write_index represents the number of unique elements
        return write_index
