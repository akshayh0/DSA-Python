class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Step 1: Initialize tortoise and hare pointers
        tortoise = nums[0]
        hare = nums[0]
        
        # Step 2: Find the intersection point in the cycle
        while True:
            tortoise = nums[tortoise]          # Moves 1 step
            hare = nums[nums[hare]]            # Moves 2 steps
            if tortoise == hare:
                break
                
        # Step 3: Find the entrance to the cycle (the duplicate number)
        tortoise = nums[0]                     # Reset tortoise to start
        while tortoise != hare:
            tortoise = nums[tortoise]          # Both move 1 step now
            hare = nums[hare]
            
        return tortoise
