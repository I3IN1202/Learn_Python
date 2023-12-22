#number, bool, string, tuple
person = {'name' : 'Minh Huy',
          'age' : 20,
          'job' : 'intern',
          1 : 'abc',
          (2,3) : 100
          }

print({key for key in person})      #key
print({person[key] for key in person}) #value
print(person.keys()) #lấy key hoặc value
print(person.items())

p1, p2, p3, p4, p5 = person
print(p1, p2, p3, p4, p5)

#sửa đổi trong dict
person['address'] = 'Thanh Xuan' #thêm
person.update({'weigh' : 65, 'height': 1.7}) #sửa
person.pop('job') #bỏ

for key in person:
    print(key, ': ', person[key])