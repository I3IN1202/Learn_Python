a = [5.5, "Đỗ", 2, "Minh", 0, 6, [2, 3, 4], False,"Huy", [1,2], True, 1.13]

t = tuple(a[::-1])
print("Ket qua 1:", t)

print("Ket qua 2: ")
for i in range(0, len(a), 3):
    print(tuple(a[i:i+3]))

print("Ket qua 3:")

for i in range(len(a)-1):
    if isinstance(a[i], tuple) and isinstance(a[i+1], tuple) and type(a[i][0]) == type(a[i+1][0]):
        print((a[i][0], a[i+1][0]))
    elif isinstance(a[i], tuple) and isinstance(a[i+1], tuple) and type(a[i][1]) == type(a[i+1]):
        print((a[i][0], a[i+1][0]))

