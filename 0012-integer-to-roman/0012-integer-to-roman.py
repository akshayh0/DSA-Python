class Solution:
    def intToRoman(self, num: int) -> str:
        # Map values to their corresponding Roman symbols in descending order
        val_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        roman_numeral = []
        
        # Loop through each value-symbol pair
        for value, symbol in val_map:
            # Stop early if num becomes 0
            if num == 0:
                break
            # Determine how many times the current symbol fits into num
            count = num // value
            if count > 0:
                roman_numeral.append(symbol * count)
                num -= value * count
                
        return "".join(roman_numeral)
