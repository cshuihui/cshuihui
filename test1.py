#replace 替换
str = '123456 123789'
#str = str.replace('123', '111')
print(f'{str.replace("123", "111")}')
#split 拆分
ls = str.split(sep = ' ')
print(ls)
#strip 去掉前后的指定字符
newstr = str.strip('19')
print(newstr)
#str[i] 索引
str1 = 'I love Nahida'
print(str1[5:])#正向索引从0开始
print(str1[-6])#反向索引从-1开始
print(str1[:5])#这种似乎右边那个是闭区间，取不到13,0>=i>13反过来也是一样
print(str1[-13:-1])

#ord 返回字符的unicode值
print(ord('a'))
#len() 返回字符串或者列表元素总长度
#str.maketrans(str1, str2)为制作一个映射表，从str1的字符映射到str2
""".translate(str.maketrans(str1, str2))就是以这个映射表的规则给字符串进行映射"""
str2 = '1234'
str3 = '5678'
text1 = '1423214'
table = ''.maketrans(str2, str3)
print('%s'%(text1.translate(table)))