class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        index = 0
        
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
            
        # Step 3: Conversion & Rounding
        result = 0
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            # Check overflow/underflow before multiplying
            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN
                
            result = result * 10 + digit
            index += 1
            
        return sign * result
