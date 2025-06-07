def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False。减小判定区间，减少循环次数，提升效率"""
    # ======================Begin=================================
    # 补充你的代码
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    # =========================End==============================


def tran(number):
    l = []
    s = number
    a = 0
    while s >= 1:
        l.append(s % 10)
        int(s / 10)
    for i in range(1, len(l) + 1):
        a += l[i - 1] * (10 ** (len(l) - i))
    if a == number:
        return True
    else:
        return False


def plalindrome_prime(number):
    """接收一个正整数参数number，遍历从0到number之间的所有整数，
    若某个数是素数，且转为字符串后是回文字符串，则称其中回文素数
    找出并在同一行中输出小于number的所有回文素数，每个数字后一个空格，函数无返回值。"""
    # ======================Begin=================================
    # 补充你的代码
    l = []
    for i in range(0, number + 1):
        if is_prime(i) and tran(i):
            l.append(i)
    for i in l:
        print(i, end=" ")

    # =========================End==============================


positive_int = int(input())
plalindrome_prime(positive_int)      
