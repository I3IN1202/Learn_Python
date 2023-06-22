#for i in range(1, 11):
# range (n) -> 0 ... n - 1
# range (x, n) -> x ... n - 1
# range (x, n, s) -> x x+s x+2s... 

#i = 1
#while i <= 10 :
#    print("hihi", i)
#    i = i + 1    

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
    if i == 6:
        break
    print(i)  
