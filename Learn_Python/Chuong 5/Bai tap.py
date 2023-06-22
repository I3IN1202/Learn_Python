n = int(input("Nhap n: "))
b = 0
count = 0
sum = 0
while n>0:
    digit = n % 10
    b = b *10 + digit
    count = count + 1
    sum = sum + digit
    n = n // 10  
print(b)
print("So n co", count, "chu so")
print(sum)

x = int(input("Nhap vi tri muon lay:"))
if x <= 0:
    print("Vị trí không hợp lệ!")
else:
    num_of_digits = 0
    num_copy = n
    while num_copy > 0:
        num_of_digits += 1
        num_copy //= 10
    if x > num_of_digits:
      print("Invalid")
    else:
        digit = 0
        for i in range(x):
            digit = n % 10
            n //= 10
print(digit)

