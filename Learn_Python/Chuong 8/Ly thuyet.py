#8F
x = ['Do', 'Minh', 'Huy']
print(' '.join(x))
y = 'Do Minh Huy sieu dep trai'
print(y.split(' '))
y = [sentence.capitalize() for sentence in x]
print(y)

#8G - phep toan
x = 'Minh Huy'
y = 'Bin'
z = ['Huy', 'Bin', 'Linh', 'Nam', 'Ngan']
print(x>y)  #so sanh chuoi: vi tri chu cai dau trong Character map
print(sorted(z))
print(sorted(x, reverse=True))

#8H
x = 'Minh \\Huy'
print(x)

#8F
import re

s = 'abcde acbde abbde acccde axyze a123e a@!#e'
pattern = 'a[\w]{2,3}e'
# . [] * + ? {} \ | ^ $
print(re.findall(pattern, s))

#regex tester:
# + : lap 1 lan tro len
# * : lap tat ca
# {}: so lan lap
# ? : 1 hoac 2
# \w : [a-zA-Z0-9] >< \W
#\s : space
# split cat chuoi
# findall, split, sub
