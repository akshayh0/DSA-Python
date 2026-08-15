# count the numer of digits using log 
import math
def count_digits(n):
    return math.floor(math.log10(n)) + 1
n = 5438
print(count_digits(n))
