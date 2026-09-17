class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                # Swap elements at low and mid, then move both pointers forward
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # The element is already in the correct relative position, move mid forward
                mid += 1
            else:  # nums[mid] == 2
                # Swap elements at mid and high, decrement high pointer
                # Do NOT increment mid here because the new nums[mid] needs to be evaluated
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
