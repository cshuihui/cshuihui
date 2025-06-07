#列表有编号编号对应值，集合里的元素位置不固定没有下标，不会重复，可用add和discard增删元素，字典有键值对，键（key）不会重复，值可以，（逻辑上无序）
#append,insert,extand，pop，remove，clear(清空列表),，del list(i)(删除第i个)(可迭代对象)用于列表
#add(),update([多个元素])，discard，remove(元素)不存在时报错，pop()(随机删除一个元素)，clear()删除整个集合，集合用
#dict[key] = val 添加新键或者更改已有值，update({})批量添加或更新，pop(key[,default]),del,clear
#.pop(key, default)删除key对应的值，若不存在返回default，可用于字典和集合
#.discard(source)删除source值，没有并不会报错，只能用于集合
#del dict[key]只能用于字典，找不到会报错，配合if语句使用可防止报错
#元组是一种不可改变的列表
import random
from collections import OrderedDict
from sys import getsizeof
from random import randint #randint是random库里的一个函数，直接import的话就是.random.randint()
student = dict()#创建空字典
name = ["纳西妲","灰灰"]
names = ["小草神","纳西妲的狗"]
mydict = dict(zip(name, names))
for a in mydict.keys():
    print("%s是%s"%(a, mydict[a]))
dicts = dict()
#for i in range(1000000):
  #  dicts[randint(1,1000000)] = randint(1,1000000)#闭区间1到1000000

#print(dicts)
print(zip(name, names))#zip封装成一个可迭代对象,打开才能用
print(dict(zip(name, names)))

