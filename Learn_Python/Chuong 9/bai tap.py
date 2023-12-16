a = map(int, input("Nhap 1 set: ").split())
a = set(a)
# #Ket qua 1:
print("Ket qua 1: ",sum(a))

# #Ket qua 2:
chan = {x for x in a if x%2==0}
le = {y for y in a if y%2!=0}
print("Ket qua 2: ", chan, le)

# #Ket qua 3:
print("Ket qua 3: ",list(sorted(a)))

#Ket qua 4:
tang_dan = all(n-m==1 for m,n in zip(sorted(a), sorted(a)[1:]))
if tang_dan:
    print("Ket qua 4: Tang deu")
else:
    print("Ket qua 4: Khong tang deu")