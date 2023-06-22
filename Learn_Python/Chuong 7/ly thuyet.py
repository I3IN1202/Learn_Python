#x = 1, 2, 3, "abc", True # tuple
#x = (1, "Minhhuy", 1.65, [90, 60, 90] )
#for index, value in enumerate(x) :
#     print(index, value)
x = [  1, 2, 3] 
x = tuple(element * 10 + element for element in x)
print(x)

# expr(element) for element in interable (tuple/list/set/dict/enumerate)