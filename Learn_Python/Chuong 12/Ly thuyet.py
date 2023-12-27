# Class and Object
s = 'Minh Huy'
print([element for element in range(10)])

# multable id khác nhau
# tạo ra 2 object khác nhau có thể thay đổi được
# phép gán python làm việc với reference
x = [1, 2, 3]
y = [1, 2, 3]
print(id(x))
print(id(y))
# inmutable id giống nhau

# def add(number):
#     number[0] = 10
# add(x)
# print(x)

#so sánh 2 object khác nhau
print(x == y , x is y)

# user define 
class Person:
    def __init__(self, name, age):
        print('haha')
        self.name = name
        self.age = age

    def hello(self):
        print('Hello, I am', self.name)


x = list()
t = set()
huy = Person('Minh Huy', 21)
linh = Person('Linh', 21)
huy.hello()
#print(huy.name, huy.age)

