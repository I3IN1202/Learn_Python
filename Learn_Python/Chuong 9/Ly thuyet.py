#set
#so sanh list voi set
x = [1, 2, 2, 3, 4, 3, 2] #list co the cung gia tri
y = () #tuple
a = {1, 2, 2, 3, 4, 3, 2} 

#for element in a:
#    print(element)
#print(sorted(a)) #sum, min, max, sorted
#print(1 in a)

a.add(1.5)
#a.update()
a.discard(2)
#a.remove() neu khong co trong set thi loi

print(a)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# |, union: hợp
# &, intersction: giao
# a \ b: difference
# a ^ b: hiệu đối xứng

print(a ^ b)