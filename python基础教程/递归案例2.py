import time

# 字符串反转
s = "你真好看"

print(s)


# print(s[::-1])


def rvs(s):
    print(s)
    if s == "":
        return s
    else:
        return rvs(s[1:]) + s[0]


print(rvs(s))

# 斐波那契数列
m = 10


def fib(n):
    print(n)
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(m))

time.sleep(100)

# 汉诺塔问题