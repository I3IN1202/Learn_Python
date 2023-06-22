x = list(map(int, input("Nhập list: ").split()))
a = 0
dem = 0
for i in range(len(x)):
    if  i % 2 == 0:
      a += x[i]
      dem += 1
print(a/dem)

b = 0
count = 0
for i in range(len(x)-1):
   if i % 2 != 0:
    count += 1
   if x[i] % 2 != 0:
     b += x[i]
print(b/6)

max = x[0]
for i in range(1, len(x)):
  if x[i] > max:
    max = x[i]
print(max)

min = x[0]
for i in range(1, len(x)):
  if x[i] < min:
    min = x[i]
print(min)

c = 0
import math
for i in range(1, len(x)):
  if math.sqrt(x[i]) == int(math.sqrt(x[i])):
    c += 1
print(c)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

lst = [0, 5, 7, 3, 9, 8]

for n in lst:
    if is_prime(n):
        print(n, sep='')
z = x
print(sorted(z))
