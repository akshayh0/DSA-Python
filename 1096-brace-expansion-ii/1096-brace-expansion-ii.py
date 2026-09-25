class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack stores: [current_group_unions, current_concatenation_level]
        stack = []
        current_group = set()
        current_res = {""}
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char.isalpha():
                # Form the word (handles single letters or strings)
                word = ""
                while i < len(expression) and expression[i].isalpha():
                    word += expression[i]
                    i += 1
                i -= 1 # Adjust for the outer loop's increment
                
                # Multiply current result by the new word
                current_res = {prefix + word for prefix in current_res}
                
            elif char == '{':
                # Save the current state to stack before entering a new group
                stack.append((current_group, current_res))
                current_group = set()
                current_res = {""}
                
            elif char == '}':
                # Finish the last part of the inner group and combine all its unions
                inner_group_total = current_group | current_res
                
                # Pop the outer context
                prev_group, prev_res = stack.pop()
                
                # Multiply the outer result with the completely evaluated inner group
                current_res = {p + suffix for p in prev_res for suffix in inner_group_total}
                current_group = prev_group
                
            elif char == ',':
                # Add the current term to the running union of this group level
                current_group |= current_res
                current_res = {""}
                
            i += 1
            
        # Final union of the top-level expression
        final_set = current_group | current_res
        
        # Return sorted list as required by the problem statement
        return sorted(list(final_set))
