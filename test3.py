arr = list(range(0, 10))
print(arr[-3:])
l1,l2,l3 = arr[:3]#拆包
print(l1,l2,l3)
l1,l2,*other = arr
print(l1,l2)
print(other)
#zip()把两个列表合并在一起
#.insert()插入元素
#.append()末尾添加
#.extend()把括号里的列表里的元素添加
#.pop()删除

#.index()找到该列表中元素第一次出现的位置
#.count()元素出现的次数
#.sort(key=len（根据元素长度排序）)排序key设置排序规则