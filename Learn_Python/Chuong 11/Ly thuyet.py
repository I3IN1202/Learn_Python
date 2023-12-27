#function
person = {
    'name' : 'Huy',
    'height' : 1.7,
    'weight' : 65
}

x = 1 #global scope
# def show_helth():
#     # BMI
#     result = '' #function scope/local scope
#     bmi = person['weight'] / person['height'] ** 2
#     if bmi < 18.5:
#         result = 'Thieu Can'
#     elif 18.5 <= bmi <=24.9:
#         result = 'Binh Thuong'
#     else:
#         result = 'Thua Can'
#     print(bmi, result)
#     global x
#     x += 1
#     print(x)
# Muon sua global thi phai khai bao global


# Parameter

# def get_bmi(w, h):
#     result = w/ h ** 2
#     return result

get_bmi = lambda w,h : w/h**2 #lambda function
get_conclusion = lambda bmi,a,b : \
    'Thieu can' if bmi < a else ('Binh thuong' if a <= bmi <= b else 'Thieu can')

def show_helth(weight, height):
    if weight <=0 or height <= 0:
        return
    # BMI
    result = '' 
    bmi = get_bmi(weight, height)
    # if bmi < 18.5:
    #     result = 'Thieu Can'
    # elif 18.5 <= bmi <=24.9:
    #     result = 'Binh Thuong'
    # else:
    #     result = 'Thua Can'
    result = get_conclusion(bmi, 18.5, 24.9)
    return bmi, result

print(show_helth(70, 1.7))
show_helth(65, 1.7)

# return
import math
x = [2, 3, 4]
y = {'a' : 2, 'b' : 3, 'c' : 4}
# Optional parameter
def hello(a, b, c = 3):
    # return a*b*c
    return math.prod(x)
hi = lambda a,b,c : a*b*c
# print(hello (1,2)) 

# unpacking
print(hello(*x))
print(hello(**y))
# built-in fuction
