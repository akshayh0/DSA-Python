n = 153 
num = n          
nod = len(str(n))
total = 0

while num > 0:
    ld = num % 10
    total = total + (ld ** nod) 
    num = num // 10        

print("Total sum of powers:", total)
if total == n:
    print(f"{n} is an Armstrong number!")
else:
    print(f"{n} is not an Armstrong number.")
