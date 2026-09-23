class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Return an empty list if the input string is empty
        if not digits:
            return []
            
        # Map digits to their corresponding telephone letters
        digit_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, current_combination: list[str]):
            # If the current combination length matches the input length, we found a valid combination
            if len(current_combination) == len(digits):
                result.append("".join(current_combination))
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            letters = digit_map[current_digit]
            
            # Explore all possible letters for the current digit
            for letter in letters:
                current_combination.append(letter)   # Choose
                backtrack(index + 1, current_combination)  # Explore
                current_combination.pop()             # Unchoose (Backtrack)
                
        # Start the backtracking process from index 0
        backtrack(0, [])
        return result
