text = 'I love Nahida!1027'
numbers = 0
alphas = 0
blanks = 0
others = 0
print(f'长度为：{len(text)}')
#upper 大写 lower 小写
for ch in text:
    if ch.isnumeric():
        numbers += 1
    elif ch.isalpha():
        alphas += 1
    elif ch.isspace():
        blanks += 1
    else:
        others += 1
print(f'数字为：{numbers}\n字母为：{alphas}\n空格为：{blanks}\n其他为：{others}')

print(f'{text[1:]}')