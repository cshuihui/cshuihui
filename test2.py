#%为占位符
from colorama import Fore
age = 500
name = '纳西妲'
print('我叫%s，今年%d岁了'%(name, age))
#format
print('我叫{}，今年{}岁了'.format(name, age))
#格式
pi = 3.14159
print('π={:.2f}'.format(pi))#8是位宽，'.'也算一位