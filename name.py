name = ['曾启明','傅馨融','黄昌鸿','周稀艳','秦志鹏','周宇康','骆超宇','周童','刘珍伶','周映熙','宁佐涵','李紫荷','邓建荣','刘念','胡超','曾媛媛','王芸芝','宋婉婷','张铭航','陈烨','邓家涛','覃聪','周思凯','侯靖宇','陈翔','马振凯','方伟','肖梓俊','杨昊','彭浩安','欧阳桦泽','苟义力','黄慧玲','陈沪欣','杜杰','孙卢山','彭欣怡']
a = input()
sum = 0
for i in name:
    if len(i) == 4:
        if i[0] + i[1] == a:
            sum += 1
    else:
        if i[0] == a:
            sum += 1
print(sum)
