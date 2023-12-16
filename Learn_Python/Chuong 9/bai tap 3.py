a = {0, 1, 2, 3, 4, 5, 6, 7, 12}
b = {0, 2, 4, 6, 8, 10}
c = {0, 3, 6, 9, 12}
d = {0, 1, 3, 5, 6, 7, 9, 11, 12}
e = {10, 9, 6, 0, 1, 2, 5}

x = [a, b, c, d, e]
#Ket qua 1
common = a.intersection(b).intersection(c).intersection(d).intersection(e)
print("Kết quả 1: ",common)

#Ket qua 2
largest_set = max(x, key=len)
print("Ket qua 2: ",len(largest_set))

#Ket qua 3
min_value = min(min(set) for set in x)
print("Ket qua 3: ", min_value)