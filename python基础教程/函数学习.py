def 阶乘(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s

#


if __name__ == "__main__":
    target = input("请输入需要阶乘的数字:\n")  # input函数是输入字符串，需要用eval函数来去掉引号
    print("{}的阶乘是{}".format(target, 阶乘(eval(target))))

    target2 = int(input("请输入需要阶乘的数字:\n"))  # input函数是输入字符串,int强制归因整数型
    print("{}的阶乘是{}".format(target2, 阶乘(target2)))
