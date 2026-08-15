num = 5873
n = num
while n > 0:
    last_dig = n % 10
    print(last_dig, end = "")
    n = n // 10