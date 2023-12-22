d = {"ab" : 12,
    "cd" : 5.2,
    "ef" : 100,
    "gh" : "ab",
    "ik" : False,
    "mno" : [1, 2, 3],
    "pq" : "ab",
    "xyz" : "Minh Huy",
    "www" : "coder"}
s = input("Enter a string: ")

#Ket qua 1
if s in d:
    print("Ket qua 1: True")
else:
    print("Ket qua 1: False")


#Ket qua 2
key = [key for key, value in d.items() if value == s]    
print(f"Ket qua 2: {key}")

#Ket qua 3
print("Ket qua 3:",[value for value in d.values() if isinstance(value, str)])

#Ket qua 4
print("Ket qua 4:",{value for value in d.values() if isinstance(value, (int,float))})