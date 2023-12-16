a = set(map(str, input("Nhap set a: ").split(';')))
b = set(map(str, input("Nhap set b: ").split(';')))

#Ket qua 1:
chung = a.intersection(b)
print(chung)

#ket qua 2:
c = a.symmetric_difference(b)
print(c)

#Ket qua 3:
name1 = set(name.split()[1] for name in a)
name2 = set(name.split()[1] for name in b)
common = name1.intersection(name2)

print (common)