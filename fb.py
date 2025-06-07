def fb(index):
    lt = [0, 1]
    for i in range(0, index):
        lt.append(lt[i] + lt[i + 1])
        print(lt[i], end=" ")


index = int(input())
fb(index)
print(list(range(2, 2)))