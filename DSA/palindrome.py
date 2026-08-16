# Check whether a number is a palindrome

n = 1234
num = n
result = 0

while num > 0:
    ld = num % 10
    result = (result * 10) + ld
    num = num // 10

if n == result:
    print("Palindrome")
else:
    print("Not a palindrome")