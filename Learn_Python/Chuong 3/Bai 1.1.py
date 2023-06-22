
x = 2
y = x - 0.5
print (int(y) == x)

x = 0
x +=1
b = x == 1
print(b)

x = -1
y = x * x + abs(x) * 2
print( y % 2)

x = 1
y = 2
z = 3
t = 3 * (z + (x+y) * (y+z))
print(1 - 2 * t )

x = 1
y = 2
z = 3
b = (x<y) or (x>z) and ((y<z) or (x<z))
print(b)

x = 1
y = x + 1
z = x + y + 1
print(int(z))

x = 1.5
y = int(x)
z = str(y)
w = "abc"
print(z + w)

x = int(1.5)
y = float(x)
print (str(y))
